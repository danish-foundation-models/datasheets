from pathlib import Path

from datasheets.datasheet import DataSheet
from datasheets.update_descriptive_statistics import find_latest_dataset_version

root_path = Path(__file__).parent.parent.parent
main_readme = root_path / "README.md"

main_sheet = DataSheet.load_from_path(main_readme)

DATASET_NAMES = [
    cfg["config_name"]
    for cfg in main_sheet.frontmatter["configs"]
    if cfg["config_name"] != "default"
]


def get_dataset_path(dataset_name: str) -> Path:
    dataset_data_path = root_path.parent / "datasets" / dataset_name
    latest_version_dataset_path = find_latest_dataset_version(dataset_data_path)

    assert latest_version_dataset_path, (
        f"Something went wrong with the {dataset_name} dataset"
    )

    return latest_version_dataset_path


def get_all_datasets() -> dict:
    load_kwargs = {
        "path": "parquet",
        "split": "train",
        "columns": ["id", "text", "token_count", "source"],
    }
    dataset_paths = []
    for dataset in DATASET_NAMES:
        dataset_path = get_dataset_path(dataset)
        files = [str(p) for p in dataset_path.glob("*.parquet")]
        dataset_paths.extend(files)
        load_kwargs["data_files"] = dataset_paths

    return load_kwargs
