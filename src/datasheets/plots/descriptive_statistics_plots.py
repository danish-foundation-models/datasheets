import logging
from pathlib import Path
from typing import cast

import numpy as np
import pandas as pd
import plotnine as pn
import plotly.graph_objects as go
from datasets import Dataset

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
