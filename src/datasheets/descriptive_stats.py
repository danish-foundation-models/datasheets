import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Self, Any
from functools import partial

from datasets import Dataset
from transformers import AutoTokenizer

from datasheets.dataset_structure import ColumnNames

from datasheets.git_utilities import (
    get_current_revision,
)

logger = logging.getLogger(__name__)


def _tokenize_function(
    examples: dict[str, Any], tokenizer: AutoTokenizer
) -> dict[str, Any]:
    token_count = [
        len(tokens)
        for tokens in tokenizer(examples[ColumnNames.text.value], padding=False)[  # type: ignore
            "input_ids"
        ]
    ]
    examples[ColumnNames.token_count.value] = token_count
    return examples


def add_token_count(
    ds: Dataset,
    tokenizer_name: str = "AI-Sweden-Models/Llama-3-8B-instruct",
    num_proc: int = 4,
) -> Dataset:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, use_fast=True)

    tokenize = partial(_tokenize_function, tokenizer=tokenizer)  # type: ignore

    ds = ds.map(tokenize, batched=True, num_proc=num_proc)
    return ds


def calculate_average_document_length(
    dataset: Dataset, text_column: str = "text"
) -> float:
    texts = sum(len(t) for t in dataset[text_column])
    return texts / len(dataset)


@dataclass()
class DescriptiveStatsOverview:
    number_of_samples: int
    average_document_length: float
    number_of_tokens: int

    @classmethod
    def from_disk(cls, path: Path):
        with path.open("r") as f:
            data = json.load(f)
        if "revision" in data:
            data.pop("revision")
        obj = cls(**data)
        return obj

    def to_disk(self, path: Path):
        data = self.__dict__
        data["revision"] = get_current_revision()
        with path.with_suffix(".json").open("w") as f:
            json.dump(self.__dict__, f, indent=2)

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> Self:
        return cls(
            number_of_samples=len(dataset),
            average_document_length=calculate_average_document_length(dataset),
            number_of_tokens=sum(dataset["token_count"]),
        )
