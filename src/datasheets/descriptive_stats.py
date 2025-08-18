from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pathlib import Path

from datasets import Dataset
import polars as pl
from polars import LazyFrame

logger = logging.getLogger(__name__)


def calculate_average_document_length(
    dataset: Dataset, text_column: str = "text"
) -> float:
    texts = sum(len(t) for t in dataset[text_column])
    return texts / len(dataset)


@dataclass()
class DescriptiveStatsOverview:
    """
    Overview of descriptive statistics for a dataset.
    Attributes:
        number_of_samples: Total number of samples in the dataset.
        number_of_tokens: Total number of tokens in the dataset
        min_length: Minimum document length in tokens.
        max_length: Maximum document length in tokens.
        average_document_length: Average document length in tokens.
    """

    number_of_samples: int
    number_of_tokens: int
    min_length_tokens: int
    max_length_tokens: int
    number_of_characters: int
    min_length_characters: int
    max_length_characters: int

    @property
    def average_document_length_tokens(self) -> float:
        return (
            self.number_of_tokens / self.number_of_samples
            if self.number_of_samples > 0
            else 0.0
        )

    @property
    def average_document_length_characters(self) -> float:
        return (
            self.number_of_characters / self.number_of_samples
            if self.number_of_samples > 0
            else 0.0
        )

    @classmethod
    def from_disk(cls, path: Path) -> DescriptiveStatsOverview:
        with path.open("r") as f:
            data = json.load(f)
        obj = cls(**data)
        return obj

    def to_disk(self, path: Path) -> None:
        with path.with_suffix(".json").open("w") as f:
            json.dump(self.__dict__, f, indent=2)

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> DescriptiveStatsOverview:
        dataset = dataset.map(
            lambda x: {
                "sum_char_count": [sum([len(t) for t in x["text"]])],
                "min_char_count": [min([len(t) for t in x["text"]])],
                "max_char_count": [max([len(t) for t in x["text"]])],
                "sum_token_count": [sum(x["token_count"])],
                "min_token_count": [min(x["token_count"])],
                "max_token_count": [max(x["token_count"])],
                "length": [len(x["text"])],
            },
            batched=True,
            num_proc=4,
            remove_columns=dataset.column_names,
        )
        return cls(
            number_of_samples=sum(dataset["length"]),
            number_of_tokens=sum(dataset["sum_token_count"]),
            min_length_tokens=min(dataset["min_token_count"]),
            max_length_tokens=max(dataset["max_token_count"]),
            number_of_characters=sum(dataset["sum_char_count"]),
            min_length_characters=min(dataset["min_char_count"]),
            max_length_characters=max(dataset["max_char_count"]),
        )

    @classmethod
    def from_dataframe(cls, df: LazyFrame) -> DescriptiveStatsOverview:
        # Pass 1: counts for token_count
        token_stats = (
            df.select(
                pl.count().alias("n_samples"),
                pl.col("token_count").cast(pl.Int64).sum().alias("n_tokens"),
                pl.col("token_count").cast(pl.Int64).min().alias("min_tok"),
                pl.col("token_count").cast(pl.Int64).max().alias("max_tok"),
            )
            .collect(engine="streaming")
            .row(0, named=True)
        )

        # Pass 2: counts for text length
        char_stats = (
            df.select(
                pl.col("text").str.len_bytes().sum().alias("n_chars"),
                pl.col("text").str.len_bytes().min().alias("min_chars"),
                pl.col("text").str.len_bytes().max().alias("max_chars"),
            )
            .collect(engine="streaming")
            .row(0, named=True)
        )

        return cls(
            number_of_samples=token_stats["n_samples"],
            number_of_tokens=token_stats["n_tokens"],
            min_length_tokens=token_stats["min_tok"],
            max_length_tokens=token_stats["max_tok"],
            number_of_characters=char_stats["n_chars"],
            min_length_characters=char_stats["min_chars"],
            max_length_characters=char_stats["max_chars"],
        )

    def __add__(self, other: DescriptiveStatsOverview) -> DescriptiveStatsOverview:
        if not isinstance(other, DescriptiveStatsOverview):
            raise TypeError("Can only add DescriptiveStatsOverview objects")
        return DescriptiveStatsOverview(
            number_of_samples=self.number_of_samples + other.number_of_samples,
            number_of_tokens=self.number_of_tokens + other.number_of_tokens,
            min_length_tokens=min(self.min_length_tokens, other.min_length_tokens),
            max_length_tokens=max(self.max_length_tokens, other.max_length_tokens),
            number_of_characters=self.number_of_characters + other.number_of_characters,
            min_length_characters=min(
                self.min_length_characters, other.min_length_characters
            ),
            max_length_characters=max(
                self.max_length_characters, other.max_length_characters
            ),
        )
