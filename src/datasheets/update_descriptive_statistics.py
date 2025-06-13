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
from datasheets.tables import create_overview_table, create_overview_table_str

logger = logging.getLogger(__name__)

main_sheet = DataSheet.load_from_path(repo_path / "README.md")
_datasets = [
    cfg["config_name"]  # type: ignore
    for cfg in main_sheet.frontmatter["configs"]  # type: ignore
    if cfg["config_name"] != "default"  # type: ignore
]


logger = logging.getLogger(__name__)


def find_latest_dataset_version(dataset_parent_path: Path) -> Path | None:
    """
    Finds the path to the latest version of a dataset within a given directory.

    Args:
        original_dataset_parent_path: A Path object pointing to the data directory

    Returns:
        A Path object to the directory of the latest version (e.g., Path(".../original/v2.0.0")),
        or None if the data directory does not exist, or no valid version folders are found.
    """
    if not dataset_parent_path.is_dir():
        logger.warning(
            f"Provided path is not a directory or does not exist: {dataset_parent_path}"
        )
        return None

    found_versions = []
    # Regex to match 'v' followed by a version string (e.g., "v1.2.3", "v1.0.0-rc1")
    # We capture the version string itself (without the 'v') to pass to packaging.Version
    version_folder_pattern = re.compile(r"^v(.+)$")

    for item in dataset_parent_path.iterdir():
        if item.is_dir():
            match = version_folder_pattern.match(item.name)
            if match:
                version_string_without_v = match.group(
                    1
                )  # Extract "1.0.0", "2.0.0-beta" etc.
                try:
                    # Parse the version string using packaging.version.Version for robust comparison
                    parsed_version = Version(version_string_without_v)
                    found_versions.append((parsed_version, item))
                except InvalidVersion:
                    # Log if a folder looks like a version but cannot be parsed by packaging
                    logger.debug(
                        f"Skipping invalid version string in folder name: {item.name}"
                    )
            else:
                # Log if a folder doesn't match the expected 'v' prefix
                logger.debug(f"Skipping non-versioned directory: {item.name}")

    if not found_versions:
        logger.info(f"No valid versioned directories found in: {dataset_parent_path}")
        return None

    # Find the maximum version using the parsed Version objects for correct semantic comparison
    latest_version_obj, latest_version_path = max(found_versions, key=lambda x: x[0])

    logger.info(
        f"Found latest dataset version: '{latest_version_path.name}' "
        f"({latest_version_obj}) in '{dataset_parent_path}'"
    )
    return latest_version_path


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
    metadata_base_path = (
        repo_path / "data" / dataset_name if dataset_name != "default" else repo_path
    )
    desc_stats_filename = "descriptive_stats.json"

    if dataset_name == "default":
        readme_name = "README.md"
    else:
        readme_name = f"{dataset_name}.md"

    desc_stats_path = metadata_base_path / desc_stats_filename
    markdown_path = metadata_base_path / readme_name

    rev = get_latest_revision(repo_path)

    if desc_stats_path.exists() and force is False:
        with desc_stats_path.open("r") as f:
            last_update = json.load(f).get("revision", None)

        if last_update is None:
            logger.warning(f"revision is not defined in {desc_stats_path}.")
        elif check_is_ancestor(ancestor_rev=last_update, rev=rev):
            logger.info(
                f"Descriptive statistics for '{dataset_name}' is already up to date, skipping."
            )
            return

    # TODO: Fix this!
    # Load the dataset using `data_files` when dataset_name = "default"

    load_kwargs = {"path": "parquet", "split": "train"}

    if dataset_name == "default":
        dataset_paths = []

        for dataset in _datasets:
            dataset_data_path = repo_path.parent / "datasets" / dataset / "original"
            latest_version_dataset_path = find_latest_dataset_version(dataset_data_path)
            if not latest_version_dataset_path:
                logger.warning(f"Something went wrong with {dataset}")
                continue

            files = [str(p) for p in latest_version_dataset_path.glob("*.parquet")]
            dataset_paths.extend(files)
        load_kwargs["data_files"] = dataset_paths
    else:
        dataset_data_path = repo_path.parent / "datasets" / dataset_name / "original"

        latest_version_dataset_path = find_latest_dataset_version(dataset_data_path)

        load_kwargs["path"] = str(latest_version_dataset_path)

    logger.info(
        f"Computing descriptive stats for: {dataset_name} from {latest_version_dataset_path}"
    )
    ds = load_dataset(**load_kwargs, columns=["id", "text", "token_count", "source"])
    ds = cast(Dataset, ds)
    desc_stats = DescriptiveStatsOverview.from_dataset(ds)
    desc_stats.to_disk(desc_stats_path)

    logger.info(f"Updating datasheet for: {dataset_name}")
    sheet = DataSheet.load_from_path(markdown_path)
    sheet.body = sheet.add_descriptive_stats(descriptive_stats=desc_stats)
    sheet.body = sheet.add_dataset_plots(ds, create_plot=True)

    if dataset_name == "default":
        logger.info("Updating Overview table")
        package = create_overview_table_str()
        sheet.body = sheet.replace_tag(package=package, tag="MAIN TABLE")
        create_domain_distribution_plot()

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
