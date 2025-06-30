from typing import cast

import pytest
from datasets import Dataset, load_dataset

from ..conftest import DATASET_NAMES, get_dataset_path


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
# @pytest.mark.skip("This tests currently fails")
def test_no_one_word_documents(dataset_name: str):
    dataset_path = get_dataset_path(dataset_name)
    ds = load_dataset(str(dataset_path.resolve()), split="train")
    ds = cast(Dataset, ds)

    one_word_docs = ds.filter(lambda x: x["token_count"] <= 1)

    assert len(one_word_docs) == 0, (
        f"Found {len(one_word_docs)} one-word documents in dataset '{dataset_name}'"
    )
