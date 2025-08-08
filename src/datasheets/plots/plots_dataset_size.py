import json
import logging
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

from dynaword.datasheet import DataSheet
from dynaword.paths import repo_path

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def _create_descriptive_stats_table(
    repo_path: Path = repo_path,
) -> pd.DataFrame:
    """
    Create a DataFrame from the descriptive statistics data.
    """
    p = (repo_path / "data").glob("**/*descriptive_stats.json")

    data = []
    for path in p:
        with path.open("r") as f:
            package = json.load(f)
            sheet = DataSheet.load_from_path(path.parent / f"{path.parent.name}.md")
            package["dataset_name"] = path.parent.name
            package["pretty_name"] = sheet.pretty_name
            data.append(package)

    df = pd.DataFrame(data)
    df["mean_length_tokens"] = df["number_of_tokens"] / df["number_of_samples"]
    df["mean_length_characters"] = df["number_of_characters"] / df["number_of_samples"]
    return df


def plot_dataset_size(df: pd.DataFrame) -> go.Figure:
    """Plot dataset size using a range plot with min, max, and mean token lengths."""
    # Calculate mean token length per document
    df["mean_length_tokens"] = df["number_of_tokens"] / df["number_of_samples"]

    # Create the range plot
    fig = go.Figure()

    # Add range bars (from min to max)
    for i, row in df.iterrows():
        fig.add_trace(
            go.Scatter(
                x=[row["min_length_tokens"], row["max_length_tokens"]],
                y=[row["dataset_name"], row["dataset_name"]],
                mode="lines",
                line=dict(color="lightgray", width=3),
                showlegend=False,
                hoverinfo="skip",
            )
        )

    # Add min points
    fig.add_trace(
        go.Scatter(
            x=df["min_length_tokens"],
            y=df["dataset_name"],
            mode="markers",
            marker=dict(color="lightblue", size=6, symbol="circle"),
            name="Min tokens",
            hovertemplate="<b>%{y}</b><br>Min: %{x:,} tokens<extra></extra>",
        )
    )

    # Add max points
    fig.add_trace(
        go.Scatter(
            x=df["max_length_tokens"],
            y=df["dataset_name"],
            mode="markers",
            marker=dict(color="darkred", size=6, symbol="circle"),
            name="Max tokens",
            hovertemplate="<b>%{y}</b><br>Max: %{x:,} tokens<extra></extra>",
        )
    )

    # Add mean points
    fig.add_trace(
        go.Scatter(
            x=df["mean_length_tokens"],
            y=df["dataset_name"],
            mode="markers",
            marker=dict(color="orange", size=8, symbol="diamond"),
            name="Mean tokens",
            hovertemplate="<b>%{y}</b><br>Mean: %{x:,.0f} tokens<extra></extra>",
        )
    )

    fig.update_layout(
        title="Token Length Distribution by Dataset<br><sub>Range (min-max) with mean values</sub>",
        xaxis_title="Number of Tokens (log scale)",
        xaxis_type="log",
        yaxis_title="Dataset",
        height=500,
        template="plotly_white",
        margin=dict(l=120),  # More space for dataset names
    )

    return fig


def create_dataset_size_plot() -> None:
    logger.info("Creating range plot of dataset sizes using `descriptive_stats.json`.")
    df = _create_descriptive_stats_table()
    fig = plot_dataset_size(df)

    save_path = repo_path / "images" / "dataset_size_plot.html"
    save_path_svg = repo_path / "images" / "dataset_size_plot.svg"

    logger.info(f"Saving dataset size plot to {save_path} and {save_path_svg}.")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(save_path)
    fig.write_image(save_path_svg)


if __name__ == "__main__":
    create_dataset_size_plot()
