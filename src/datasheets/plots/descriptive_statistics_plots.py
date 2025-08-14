import logging
from pathlib import Path
from typing import cast

import pandas as pd
import plotnine as pn
from datasets import Dataset
import polars as pl

from datasheets.descriptive_stats import DescriptiveStatsOverview

logger = logging.getLogger(__name__)


def create_descriptive_statistics_plots(
    dataset: Dataset,
    save_dir: Path,
) -> tuple[Path, pn.ggplot]:
    logger.info("creating descriptive statistics plot to readme.")
    # lengths = dataset["token_count"]
    df = dataset.to_pandas()
    df = cast(pd.DataFrame, df)
    df = df[["token_count", "source"]].rename(
        columns={"token_count": "lengths", "source": "Source"}
    )
    # df = pd.DataFrame({"lengths": lengths, "Source": dataset["source"]})

    plot = (
        pn.ggplot(df, pn.aes(x="lengths", y=pn.after_stat("count")))
        + pn.geom_histogram(bins=100)
        + pn.labs(
            x="Document Length (Tokens)",
            y="Count",
            title="Distribution of Document Lengths",
        )
        + pn.theme_minimal()
        + pn.facet_wrap("Source", scales="free", ncol=3)
    )

    img_path = save_dir / "images"
    img_path.mkdir(parents=False, exist_ok=True)
    save_path = img_path / "dist_document_length.png"
    pn.ggsave(
        plot,
        save_path,
        dpi=500,
        width=10,
        height=10,
        units="in",
        verbose=False,
    )

    return save_path, plot


def create_descriptive_statistics_plots_lazy(
    lf: pl.LazyFrame,          # <- accept LazyFrame instead of Dataset
    save_dir: Path,
    desc_stats: DescriptiveStatsOverview,
) -> tuple[Path, pn.ggplot]:
    logger.info("Creating descriptive statistics plot …")
    min_len = desc_stats.min_length_tokens
    max_len = desc_stats.max_length_tokens
    n_bins = 100

    if min_len is None or max_len is None:
        raise ValueError("Dataset appears to be empty or token_count is missing.")

    bin_width = (max_len - min_len) / n_bins

    # --- PASS 2: Bin and count in streaming mode ---
    binned = (
        lf.select(
            lengths=pl.col("token_count").cast(pl.Int64)
        )
        .with_columns(
            bin_idx=((pl.col("lengths") - min_len) / bin_width).floor().cast(pl.Int64)
        )
        .group_by("bin_idx")
        .agg(pl.count().alias("count"))
        .with_columns(
            bin_center=(pl.col("bin_idx").cast(pl.Float64) + 0.5) * bin_width + min_len
        )
        .sort("bin_idx")
        .collect(engine="streaming")
    )

    # --- Build plotnine plot ---
    plot = (
        pn.ggplot(binned, pn.aes(x="bin_center", y="count"))
        + pn.geom_col(width=bin_width)
        + pn.labs(
            x="Document Length (Tokens)",
            y="Count",
            title="Distribution of Document Lengths (All Sources Combined)",
        )
        + pn.theme_minimal()
)

    # --- Save image ---
    img_path = save_dir / "images"
    img_path.mkdir(parents=True, exist_ok=True)
    save_path = img_path / "dist_document_length.png"
    pn.ggsave(plot, save_path, dpi=500, width=10, height=10, units="in")

    return save_path, plot