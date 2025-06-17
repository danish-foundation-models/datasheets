import pytest
from datasets import load_dataset

from datasheets.dataset_structure import SampleSchema
from datasheets.paths import repo_path

from .conftest import DATASET_NAMES, get_dataset_path


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_sample_schema(dataset_name: str):
    """Ensure that the dataset samples follow the correct schema"""

    dataset_path = get_dataset_path(dataset_name)

    ds = load_dataset(str(dataset_path.resolve()), split="train", streaming=True)
    sample = next(iter(ds))
    SampleSchema(**sample)


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_dataset_folder_structure(dataset_name: str):
    """tests that the datasheet and dataset folder structure is as follows.

    == datasheet ==
    dataset_name
    |- dataset_name.md

    == dataset ==
    dataset_name
    |- original
    |  |- v1.0.0 (atleast)
    |  |  |- dataset_name.parquet

    If there is a python file, there should at least be one called `create.py`, but there can be additional.
    """
    metadata_path = repo_path / "data" / dataset_name
    dataset_data_path = repo_path.parent / "datasets" / dataset_name

    assert (dataset_data_path / "original").exists()
    assert (dataset_data_path / "original" / "v1.0.0").exists()
    assert (
        dataset_data_path / "original" / "v1.0.0" / f"{dataset_name}.parquet"
    ).exists()
    assert (metadata_path / f"{dataset_name}.md").exists()
    assert (metadata_path / "descriptive_stats.json").exists()

    # if any(p.name.endswith(".py") for p in path.glob("*")):
    #     assert (path / "create.py").exists()
