from typing import cast

import pytest
from datasets import Dataset, load_dataset

from .conftest import DATASET_NAMES, get_all_datasets, get_dataset_path


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_no_within_data_duplicates(dataset_name: str):
    dataset_path = get_dataset_path(dataset_name)
    ds = load_dataset(str(dataset_path.resolve()), split="train")
    ds = cast(Dataset, ds)

    assert len(set(ds["text"])) == len(ds)


@pytest.mark.skip(
    "This tests takes too long to run"
)  # there seems to be some duplicate across
def test_no_data_duplicates():
    load_kwargs = get_all_datasets()
    ds = load_dataset(**load_kwargs)
    ds = cast(Dataset, ds)

    assert len(set(ds["text"])) == len(ds)
