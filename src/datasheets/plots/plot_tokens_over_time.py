import json
import logging
import subprocess
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import plotly.graph_objects as go

from dynaword.paths import repo_path

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_file_history(
    filename: str = "descriptive_stats.json",
) -> List[Tuple[str, str, str]]:
    """Get commit history for a file with commit messages"""
    logger.info(f"Retrieving git history for {filename}")

    cmd = [
        "git",
        "log",
        "--format=%H|%ci|%s",  # commit hash | commit date | subject
        "--",
        filename,
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=repo_path, check=True
        )
        commits = []

        for line in result.stdout.strip().split("\n"):
            if line:
                parts = line.split("|", 2)  # Split on first 2 pipes only
                if len(parts) == 3:
                    commit_hash, date_str, message = parts
                    commits.append((commit_hash, date_str, message))

        logger.info(f"Found {len(commits)} commits for {filename}")
        return commits

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to get git history: {e}")
        return []


def get_file_at_commit(commit_hash: str, filename: str) -> Optional[Dict[str, Any]]:
    """Get file content at specific commit"""
    cmd = ["git", "show", f"{commit_hash}:{filename}"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=repo_path, check=True
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        logger.warning(f"Failed to parse {filename} at commit {commit_hash[:8]}: {e}")
        return None


def create_token_dataframe(filename: str = "descriptive_stats.json") -> pd.DataFrame:
    """Create DataFrame with token history from git commits"""
    logger.info("Building token history dataframe from git commits")

    commits = get_file_history(filename)
    if not commits:
        logger.warning("No commits found")
        return pd.DataFrame()

    data = []
    for commit_hash, date_str, commit_message in commits:
        file_data = get_file_at_commit(commit_hash, filename)
        if file_data and "number_of_tokens" in file_data:
            try:
                date = datetime.fromisoformat(date_str.split(" ")[0])
                data.append(
                    {
                        "date": date,
                        "tokens": file_data["number_of_tokens"],
                        "samples": file_data.get("number_of_samples", 0),
                        "avg_length": file_data.get("average_document_length", 0),
                        "commit": commit_hash,
                        "commit_short": commit_hash[:8],
                        "commit_message": commit_message,
                    }
                )
            except ValueError as e:
                logger.warning(f"Failed to parse date {date_str}: {e}")

    # Convert to DataFrame and sort by date
    df = pd.DataFrame(data)
    if df.empty:
        logger.warning("No valid data found in commits")
        return df

    df = df.sort_values("date").reset_index(drop=True)

    # Calculate token changes
    if len(df) > 1:
        df["token_change"] = df["tokens"].diff()

    logger.info(
        f"Created dataframe with {len(df)} data points spanning {df['date'].min().date()} to {df['date'].max().date()}"
    )
    return df


def _format_tokens(value: float) -> str:
    """Format tokens with human-readable suffixes"""
    if value >= 1e12:
        return f"{value / 1e12:.2f}T"
    elif value >= 1e9:
        return f"{value / 1e9:.2f}G"
    elif value >= 1e6:
        return f"{value / 1e6:.2f}M"
    elif value >= 1e3:
        return f"{value / 1e3:.2f}k"
    else:
        return f"{value:.0f}"


def _create_hover_text(df: pd.DataFrame) -> List[str]:
    """Create hover text for each data point"""
    hover_text = []
    for _, row in df.iterrows():
        hover_info = (
            f"Date: {row['date'].strftime('%Y-%m-%d')}<br>"
            f"Tokens: {_format_tokens(row['tokens'])}<br>"
        )

        if pd.notna(row.get("token_change")):
            change_sign = "+" if row["token_change"] >= 0 else ""
            hover_info += (
                f"Change: {change_sign}{_format_tokens(abs(row['token_change']))}<br>"
            )

        hover_info += (
            f"Samples: {row['samples']:,}<br>"
            f"Commit: {row['commit_short']}<br>"
            f"Message: {row['commit_message']}"
        )
        hover_text.append(hover_info)

    return hover_text


def _add_reference_lines(fig: go.Figure) -> None:
    """Add reference lines for other Danish corpora"""
    references = [
        (300_000_000, "Common Corpus (dan) (Langlais et al., 2025)"),
        (1_000_000_000, "Danish Gigaword (Derczynski et al., 2021)"),
    ]

    for y_value, annotation in references:
        fig.add_hline(
            y=y_value,
            line_dash="dash",
            line_color="gray",
            line_width=1,
            annotation_text=annotation,
            annotation_position="top left",
            annotation_font_size=12,
            annotation_font_color="gray",
        )


def plot_tokens_over_time(
    df: pd.DataFrame, width: int = 600, height: int = 400
) -> go.Figure:
    """Plot tokens over time using Plotly with interactive hover info"""
    hover_text = _create_hover_text(df)

    # Create the plot
    fig = go.Figure()

    # Add main data line
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["tokens"],
            mode="lines+markers",
            name="Tokens",
            line=dict(width=3, color="#DC2626"),  # Saturated red
            marker=dict(size=5, color="#DC2626"),
            hovertemplate="%{text}<extra></extra>",
            text=hover_text,
        )
    )

    # Add reference lines
    _add_reference_lines(fig)

    # Update layout
    fig.update_layout(
        title="Number of Tokens Over Time in Danish Dynaword",
        xaxis_title="Date",
        yaxis_title="Number of Tokens (Llama 3)",
        hovermode="closest",
        width=width,
        height=height,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
    )

    # Set x-axis and y-axis properties
    # x_min = df["date"].min() - pd.Timedelta(days=)
    # x_max = df["date"].max() + pd.Timedelta(days=1)

    # Format y-axis
    fig.update_yaxes(tickformat=".2s", ticksuffix="")
    # fig.update_xaxes(range=[x_min, x_max])  # Explicitly set x-axis range
    return fig


def create_tokens_over_time_plot() -> None:
    """Main function to create DataFrame and plot tokens over time"""
    df = create_token_dataframe()
    if not df.empty:
        logger.info("Generating interactive plot")
        fig = plot_tokens_over_time(df)
    else:
        logger.warning("No data available to plot")
        return

    save_path = repo_path / "images" / "tokens_over_time.html"
    save_path_svg = repo_path / "images" / "tokens_over_time.svg"

    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(save_path, include_plotlyjs="cdn")
    fig.write_image(save_path_svg)


if __name__ == "__main__":
    create_tokens_over_time_plot()