from collections import Counter
from typing import cast

from datasets import Dataset, load_dataset

from tests.conftest import get_all_datasets


def test_ensure_ids_are_unique():
    load_kwargs = get_all_datasets()
    ds = load_dataset(**load_kwargs)
    ds = cast(Dataset, ds)
    counter = Counter(ds["id"])
    duplicates = [item for item, count in counter.items() if count > 1]
    assert len(duplicates) == 0, f"Duplicate IDs found: {duplicates}"
