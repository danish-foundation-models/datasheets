import logging
import subprocess
import shutil
from pathlib import Path

from datasheets.paths import repo_path
from datasheets.update_descriptive_statistics import (
    find_latest_dataset_version,
    main as update_sheets,
)
from datasheets.generate_sheet import add_dataset_to_readme

download_path = repo_path.parent / "tmp"

logger = logging.getLogger(__name__)


def download_repo(
    download_path: Path = download_path,
    repo_url: str = "https://huggingface.co/datasets/danish-foundation-models/danish-dynaword",
) -> Path:
    """
    Downloads the repository from the given URL to the specified path.
    """
    logger.info(f"Downloading repository to {download_path}")
    if not download_path.exists():
        download_path.mkdir(parents=True, exist_ok=True)

    dynaword_path = download_path / repo_url.split("/")[-1]

    if dynaword_path.exists():
        logger.info("Found dynaword locally, pull latest changes.")
        subprocess.run(["git", "pull"], check=True, cwd=dynaword_path)
        logger.info("Done pulling changes.")
    else:
        logger.info("Could not find dynaword, downloads it now.")
        # Use git to clone the repository running it from the download path
        subprocess.run(["git", "clone", repo_url], check=True, cwd=download_path)
        logger.info("Download complete.")
    return dynaword_path


def copy_parquet_files(input_folder: Path, output_folder: Path):
    file_ext = ".parquet"
    logger.info(f"Copying {file_ext} from {input_folder} to {output_folder}")
    for dir in input_folder.iterdir():
        if not dir.is_dir():
            logger.warning(f"Found a file in dynaword/data: {dir}")
            continue

        dataset_name = dir.name

        if dataset_name == "lexdk":
            continue  # LexDK have been taken down, but datasheet is still available in dynaword.

        dataset_version = find_latest_dataset_version(
            output_folder / dataset_name
        )

        if not dataset_version:  # TODO: Create the new directory here instead.
            logger.warning(f"Did not find the {dataset_name} dataset. Creating folder.")
            (output_folder / dataset_name / "original" / "v1.0.0").mkdir(
                parents=True, exist_ok=True
            )
            dataset_version = output_folder / dataset_name / "original" / "v1.0.0"

        dataset_version = dataset_version.name
        logger.info(f"Moving from {dir / (dataset_name + file_ext)}")
        logger.info(
            f"Moving to: {output_folder / dataset_name / 'original' / dataset_version / (dataset_name + file_ext)}"
        )
        shutil.copy(
            dir / (dataset_name + file_ext),
            (
                output_folder
                / dataset_name
                / "original"
                / dataset_version
                / (dataset_name + file_ext)
            ),
        )


def copy_markdown_files(input_folder: Path, output_folder: Path):
    file_ext = ".md"
    logger.info(f"Copying {file_ext} from {input_folder} to {output_folder}")
    for dir in input_folder.iterdir():
        if not dir.is_dir():
            logger.warning(f"Found a file in dynaword/data: {dir}")
            continue

        dataset_name = dir.name

        if dataset_name == "lexdk":
            continue  # LexDK have been taken down, but datasheet is still available in dynaword.

        logger.info(f"Moving from {dir / (dataset_name + file_ext)}")

        # TODO: Check if destination exists, else create directory.
        destination = output_folder / dataset_name / (dataset_name + file_ext)
        if not destination.exists():
            logger.info(
                f"The {dataset_name} dataset does not exist. Creating folder and adding to readme config."
            )
            destination.parent.mkdir(parents=True, exist_ok=True)
            add_dataset_to_readme(dataset_name)

        shutil.copy(
            dir / (dataset_name + file_ext),
            destination,
        )

        logger.info(f"Moving to: {destination}")


def main():
    # Sync / Download dynaword
    dynaword_path = download_repo()

    # Iterate over data folder
    ## Copy parquet to data/dataset/{dataset_name}/original/{newest version}
    copy_parquet_files(dynaword_path / "data", repo_path.parent / "datasets")
    ## Copy datasheet to data/datasheets/data/{dataset_name}/
    copy_markdown_files(dynaword_path / "data", repo_path / "data")

    # Update main sheet with new findings
    update_sheets("default", force=True)
    pass


if __name__ == "__main__":
    log_path = repo_path / "dynaword_sync.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path),
        ],
    )
    main()
