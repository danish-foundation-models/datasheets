import logging
from pathlib import Path
import re
from typing import Literal, cast

import numpy as np
import pandas as pd
import plotnine as pn
import plotly.graph_objects as go
from datasets import Dataset
import polars as pl

from datasheets.descriptive_stats import DescriptiveStatsOverview

from datasheets.utils import convert_to_human_readable

logger = logging.getLogger(__name__)


def create_descriptive_statistics_plots(
    dataset: Dataset,
    save_dir: Path,
) -> tuple[Path, go.Figure]:
    logger.info("creating descriptive statistics plot to readme.")
    # lengths = dataset["token_count"]
    df = dataset.to_pandas()
    df = cast(pd.DataFrame, df)
    df = df[["token_count", "source"]].rename(
        columns={"token_count": "lengths", "source": "Source"}
    )
    # df = pd.DataFrame({"lengths": lengths, "Source": dataset["source"]})

    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=df["lengths"],
            nbinsx=50,  # fewer bins for cleaner look
            marker_color="lightblue",
            opacity=0.8,
        )
    )

    fig.update_layout(
        title=f"Distribution of Document Lengths for {df['Source'].iloc[0]}",
        xaxis_title="Document Length (Tokens)",
        yaxis_title="Number of Documents",
        xaxis_tickformat=",",  # comma-separate large numbers
        template="plotly_white",
    )

    # After building your fig:
    # Get current x and y tick values from Plotly's auto-generated axes
    # (We pick a reasonable range if no figure is shown yet)
    x_vals = list(range(0, int(df["lengths"].max()), int(df["lengths"].max() // 5)))[1:]

    fig.update_xaxes(
        tickvals=x_vals,
        ticktext=[convert_to_human_readable(v) for v in x_vals],
        title_text="Document Length (Tokens)"
    )

    # Compute bin counts
    counts, _ = np.histogram(df["lengths"], bins=50)
    y_max = counts.max()

    # Now generate ticks based on that max
    y_vals = list(range(0, y_max + 1, max(1, y_max // 5)))[1:]

    fig.update_yaxes(
        tickvals=y_vals,
        ticktext=[convert_to_human_readable(v) for v in y_vals],
        title_text="Number of Documents"
    )

    img_path = save_dir / "images"
    img_path.mkdir(parents=False, exist_ok=True)
    save_path_svg = img_path / "dist_document_length.svg"
    save_path = img_path / "dist_document_length.html"

    logger.info(f"Saving descriptive statistics plot to {save_path}.")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(save_path)
    fig.write_image(save_path_svg)
    # Save as SVG if needed
    # fig.write_image(save_path_svg, format="svg")
    # pn.ggsave(
    #     plot,
    #     save_path,
    #     dpi=500,
    #     width=10,
    #     height=10,
    #     units="in",
    #     verbose=False,
    # )

    return save_path, fig


def parse_bin_interval(interval_str: str, side: Literal["left", "right"]) -> float:
    # Remove brackets/parentheses
    cleaned = interval_str.strip("()[]")
    nums = cleaned.split(",")
    left, right = nums[0].strip(), nums[1].strip()

    def safe_float(val: str) -> float:
        if val == "-inf":
            val = "0"
        return float(val)

    return safe_float(left) if side == "left" else safe_float(right)


def create_descriptive_statistics_plots_lazy(
    lf: pl.LazyFrame,
    save_dir: Path,
    desc_stats: DescriptiveStatsOverview,
    dataset_name: str,
) -> tuple[Path, go.Figure]:
    logger.info("Creating descriptive statistics plot (log-spaced bins, streaming)…")
    min_len = desc_stats.min_length_tokens
    max_len = desc_stats.max_length_tokens
    n_bins = 50  # fewer bins since they grow exponentially

    if min_len is None or max_len is None or min_len <= 0:
        raise ValueError("Dataset appears to be empty or token_count is missing.")

    # --- Precompute log-spaced bin edges ---
    bin_edges = np.logspace(np.log2(min_len), np.log2(max_len), n_bins, base=2)

    # --- Assign lengths to bins using pl.cut ---
    binned = (
        lf.select(pl.col("token_count").cast(pl.Int64).alias("lengths"))
        .with_columns(
            pl.col("lengths").cut(bin_edges).alias("bin")
        )
        .group_by("bin")
        .agg(pl.count().alias("count"))
        .sort("bin")
        .collect(engine="streaming")
    )

    # Convert to pandas
    df = binned.to_pandas()

    # Parse bin edges from strings
    df["bin_left"] = df["bin"].apply(
        lambda x: parse_bin_interval(x, side="left")
    ).astype(float)
    df["bin_right"] = df["bin"].apply(
        lambda x: parse_bin_interval(x, side="right")
    ).astype(float)

    # Calculate actual bin widths for proper bar spacing
    df["bin_width"] = df["bin_right"] - df["bin_left"]

    # Handle infinite bin widths (for rightmost bin that goes to infinity)
    # Replace inf widths with a reasonable width based on the previous bin
    inf_mask = np.isinf(df["bin_width"])
    if inf_mask.any():
        # Use the width of the previous bin for the infinite bin
        prev_width = df.loc[~inf_mask, "bin_width"].iloc[-1] if len(df) > 1 else df["bin_left"].iloc[-1]
        df.loc[inf_mask, "bin_width"] = prev_width
        df.loc[inf_mask, "bin_right"] = df["bin_left"].iloc[-1] + prev_width

    # Geometric mean for log bins
    df["bin_center"] = np.sqrt(df["bin_left"] * df["bin_right"])

    # --- Build plotly chart ---
    fig = go.Figure()
    
    fig.add_trace(
        go.Bar(
            x=df["bin_center"],
            y=df["count"],
            marker_color="lightblue",
            opacity=0.8,
            width=df["bin_width"] * 0.8,
        )
    )

    fig.update_layout(
        title=f"Distribution of Document Lengths (log bins) - {dataset_name}",
        xaxis_title="Document Length (Tokens, log scale)",
        yaxis_title="Number of Documents",
        template="plotly_white",
        xaxis_type="log",
    )

    # Format x ticks (logarithmic scale, nice round powers of 10)
    x_vals = np.logspace(np.log10(min_len), np.log10(max_len), 6).astype(int)
    fig.update_xaxes(
        tickvals=x_vals,
        ticktext=[convert_to_human_readable(v) for v in x_vals],
    )

    # Format y ticks
    y_max = df["count"].max()
    y_vals = list(range(0, y_max + 1, max(1, y_max // 5)))
    fig.update_yaxes(
        tickvals=y_vals,
        ticktext=[convert_to_human_readable(v) for v in y_vals],
    )

    # --- Save image ---
    img_path = save_dir / "images"
    img_path.mkdir(parents=True, exist_ok=True)
    save_path_svg = img_path / "dist_document_length.svg"
    save_path = img_path / "dist_document_length.html"

    fig.write_html(save_path)
    fig.write_image(save_path_svg)

    return save_path, fig

