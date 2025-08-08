"""
A simple CLI to updates descriptive statistics on all datasets.

Example use:

    uv run  src/dynaword/update_descriptive_statistics.py --dataset wikisource

"""

import argparse
import json
import logging
from pathlib import Path
import re
from typing import cast
from packaging.version import Version, InvalidVersion

import plotly.express as px
from datasets import Dataset, load_dataset

from datasheets.datasheet import DataSheet
from datasheets.descriptive_stats import DescriptiveStatsOverview
from datasheets.git_utilities import (
    check_is_ancestor,
    get_latest_revision,
)
from datasheets.paths import repo_path
from datasheets.plots.plot_tokens_over_time import create_tokens_over_time_plot
from datasheets.tables import (
    create_overview_table,
    create_overview_table_str,
    create_grouped_table_str,
)

main_sheet = DataSheet.load_from_path(repo_path / "README.md")
_datasets = [
    cfg["config_name"]  # type: ignore
    for cfg in main_sheet.frontmatter["configs"]  # type: ignore
    if cfg["config_name"] != "default"  # type: ignore
]


logger = logging.getLogger(__name__)
# Define dataset type priorities (lower number = higher priority)
DATASET_TYPE_PRIORITY = {
    "processed": 1,
    "dedup": 2,
    "original": 3,
}


def find_latest_dataset_version(dataset_parent_path: Path) -> Path | None:
    """
    Finds the path to the latest dataset version based on dataset type priority and semantic version.

    Args:
        dataset_parent_path: A Path object pointing to the dataset directory (e.g., ".../datasets/mydataset")

    Returns:
        A Path object to the directory of the latest versioned dataset,
        e.g., Path(".../datasets/mydataset/processed/v2.0.0"),
        or None if nothing valid is found.
    """
    if not dataset_parent_path.is_dir():
        logger.warning(
            f"Provided path is not a directory or does not exist: {dataset_parent_path}"
        )
        return None

    version_folder_pattern = re.compile(r"^v(.+)$")

    candidates: list[tuple[int, Version, Path]] = []

    for dataset_type_dir in dataset_parent_path.iterdir():
        if not dataset_type_dir.is_dir():
            continue

        dataset_type = dataset_type_dir.name
        if dataset_type not in DATASET_TYPE_PRIORITY:
            logger.debug(f"Skipping unknown dataset type directory: {dataset_type_dir}")
            continue

        for version_dir in dataset_type_dir.iterdir():
            if not version_dir.is_dir():
                continue

            match = version_folder_pattern.match(version_dir.name)
            if not match:
                logger.debug(f"Skipping non-versioned directory: {version_dir}")
                continue

            version_str = match.group(1)

            try:
                parsed_version = Version(version_str)
                candidates.append(
                    (
                        DATASET_TYPE_PRIORITY[
                            dataset_type
                        ],  # priority (lower is better)
                        parsed_version,  # parsed Version
                        version_dir,  # full path
                    )
                )
            except InvalidVersion:
                logger.debug(
                    f"Skipping invalid version string in folder name: {version_dir.name}"
                )

    if not candidates:
        logger.info(
            f"No valid versioned dataset directories found in: {dataset_parent_path}"
        )
        return None

    # Sort by dataset type priority first (lowest = highest priority), then by version (highest version last)
    best_candidate = max(
        candidates,
        key=lambda x: (-x[0], x[1]),  # dataset type priority ASC, version DESC
    )

    _, best_version, best_path = best_candidate

    logger.info(
        f"Found latest dataset: '{best_path.parent.name}/{best_path.name}' "
        f"(type priority {best_candidate[0]}, version {best_version})"
    )
    return best_path


def create_domain_distribution_plot(
    save_dir: Path = repo_path,
):
    df = create_overview_table(
        add_readable_tokens=False, add_total_row=False, add_readme_references=False
    )
    fig = px.sunburst(df, path=["Domain", "Source"], values="N. Tokens")

    fig.update_traces(textinfo="label+percent entry")
    fig.update_layout(title="Dataset Distribution by Domain and Source")

    img_path = save_dir / "images"
    img_path.mkdir(parents=False, exist_ok=True)
    save_path = img_path / "domain_distribution.png"
    fig.write_image(
        save_path,
        width=800,
        height=800,
        scale=2,
    )


def update_dataset(
    dataset_name: str,
    force: bool = False,
) -> None:
    dataset_path = (
        repo_path / "data" / dataset_name if dataset_name != "default" else repo_path
    )

    if dataset_name == "default":
        readme_name = "README.md"
    else:
        readme_name = f"{dataset_name}.md"

    desc_stats_path = dataset_path / "descriptive_stats.json"
    markdown_path = dataset_path / readme_name

    rev = get_latest_revision(dataset_path)

    if desc_stats_path.exists() and force is False:
        logger.info(
            f"descriptive statistics for '{dataset_name}' is already exists (``{desc_stats_path}``), skipping."
        )
        return

    logger.info(f"Updating datasheet for: {dataset_name}")
    sheet = DataSheet.load_from_path(markdown_path)

    if dataset_name != "default":
        load_kwargs: dict[str, str | list[str]] = {"path": "parquet", "split": "train"}
        dataset_data_path = repo_path.parent / "datasets" / dataset_name

        latest_version_dataset_path = find_latest_dataset_version(dataset_data_path)

        if not latest_version_dataset_path:
            logger.error(f"Something went wrong in finding the {dataset_name} dataset.")
            return

        load_kwargs["path"] = str(latest_version_dataset_path)

        logger.info(
            f"Computing descriptive stats for: {dataset_name} from {latest_version_dataset_path}"
        )
        ds = load_dataset(**load_kwargs, columns=["id", "text", "token_count", "source"])  # type: ignore
        ds = cast(Dataset, ds)
        desc_stats = DescriptiveStatsOverview.from_dataset(ds)
        sheet.body = sheet.add_dataset_plots(ds, create_plot=True)
    else:
        # compute descriptive stats from existing files
        desc_paths = (repo_path / "data").glob("**/*descriptive_stats.json")
        _desc_stats = [DescriptiveStatsOverview.from_disk(p) for p in desc_paths]
        desc_stats = sum(_desc_stats[1:], start=_desc_stats[0])
    desc_stats.to_disk(desc_stats_path)

    sheet.body = sheet.add_descriptive_stats(descriptive_stats=desc_stats)

    if dataset_name == "default":
        logger.info("Updating Overview table")
        overview_table = create_overview_table_str()
        sheet.body = sheet.replace_tag(package=overview_table, tag="MAIN TABLE")
        logger.info("Updating domain table")
        domain_table = create_grouped_table_str(group="Domain")
        sheet.body = sheet.replace_tag(package=domain_table, tag="DOMAIN TABLE")
        logger.info("Updating license table")
        domain_table = create_grouped_table_str(group="License")
        sheet.body = sheet.replace_tag(package=domain_table, tag="LICENSE TABLE")
        create_domain_distribution_plot()
        create_tokens_over_time_plot()

    sheet.write_to_path()


def create_parser():
    parser = argparse.ArgumentParser(
        description="Calculated descriptive statistics of the datasets in tha data folder"
    )
    parser.add_argument(
        "--dataset",
        default=None,
        type=str,
        help="Use to specify if you only want to compute the statistics from a singular dataset.",
    )
    parser.add_argument(
        "--logging_level",
        default=20,
        type=int,
        help="Sets the logging level. Default to 20 (INFO), other reasonable levels are 10 (DEBUG) and 30 (WARNING).",
    )
    parser.add_argument(
        "--force",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Should the statistics be forcefully recomputed. By default it checks the difference in commit ids.",
    )
    return parser


def main(
    dataset: str | None = None,
    logging_level: int = 20,
    force: bool = False,
) -> None:
    logging.basicConfig(level=logging_level)

    if dataset:
        update_dataset(dataset, force=force)
    else:
        for dataset_name in _datasets:
            update_dataset(dataset_name, force=force)
        update_dataset("default", force=force)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    main(
        args.dataset,
        logging_level=args.logging_level,
        force=args.force,
    )
