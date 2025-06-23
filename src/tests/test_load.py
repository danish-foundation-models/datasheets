from datasets import load_dataset

from datasheets.datasheet import DataSheet
from datasheets.paths import repo_path

from .conftest import get_all_datasets

REMOVED_DATA = [
    "lexdk"
]  # data that has been removed due to legal disputes, question about legality, or similar

HIDDEN_DATA = [
    "ai4welfare-kb-data"  # Temporarily hidden for now, until we receive the data.
]


def test_dataset_loads():
    """Ensures that the dataset can load as intended"""
    load_kwargs = get_all_datasets()
    ds = load_dataset(**load_kwargs, streaming=True)
    sample = next(iter(ds))
    assert isinstance(sample, dict)


def test_all_datasets_in_yaml():
    ds_sheet = DataSheet.load_from_path(repo_path / "README.md")

    ds_names = {
        cfg["config_name"]
        for cfg in ds_sheet.frontmatter["configs"]
        if cfg["config_name"] != "default"
    }

    data_folder = repo_path / "data"
    datasets = data_folder.glob("*")

    for dataset in datasets:
        if dataset.name not in REMOVED_DATA + HIDDEN_DATA:
            assert dataset.name in ds_names
