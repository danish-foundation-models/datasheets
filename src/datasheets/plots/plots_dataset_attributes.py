

import logging
from pathlib import Path

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datasheets.paths import repo_path
from datasheets.tables import create_overview_table

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

LANGID_TO_LANGUAGE = {
    "en": "English", "da": "Danish"}

def create_domain_distribution_plot(
    save_dir: Path = repo_path,
):
    df = create_overview_table(
        add_readable_tokens=False, add_total_row=False, add_readme_references=False
    )
    fig = px.sunburst(df, path=["Domain", "Source"], values="N. Tokens")

    fig.update_traces(textinfo="label+percent entry")
    fig.update_layout(title="Dataset Distribution by Domain and Source")

    img_path = save_dir / "images"
    img_path.mkdir(parents=False, exist_ok=True)
    save_path = img_path / "domain_distribution.png"
    fig.write_image(
        save_path,
        width=800,
        height=800,
        scale=2,
    )


def create_language_distribution_plot(save_dir: Path = repo_path):
    df = create_overview_table(
        add_readable_tokens=False, add_total_row=False, add_readme_references=False
    )

    # Apply sqrt scaling (softens English dominance)
    # df["sqrt_tokens"] = df["N. Tokens"] ** 0.5

    # Languages list
    languages = df["Language"].unique()
    n_langs = len(languages)

    # Grid arrangement: 3 columns per row
    n_cols = min(3, n_langs)
    n_rows = -(-n_langs // n_cols)  # ceiling division

    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=languages,
        specs=[[{"type": "domain"}] * n_cols for _ in range(n_rows)],
    )

    # Define muted colors per language (extendable)
    base_colors = [
        "#4C78A8", "#72B7B2", "#F58518", "#E45756",
        "#54A24B", "#B279A2", "#FF9DA6", "#9D755D"
    ]

    color_map = {lang: base_colors[i % len(base_colors)] for i, lang in enumerate(languages)}

    # Add treemaps
    for i, lang in enumerate(languages):
        row = i // n_cols + 1
        col = i % n_cols + 1
        lang_df = df[df["Language"] == lang]

        fig.add_trace(
            go.Treemap(
                labels=lang_df["Source"].str.replace("_", "<br>").str.title(),
                parents=[""] * len(lang_df),
                values=lang_df["N. Tokens"],
                textinfo="label+percent entry",
                name=lang,
                marker=dict(colors=[color_map[lang]] * len(lang_df)),
            ),
            row=row,
            col=col,
        )

    # Layout tweaks
    fig.update_layout(
        title="Dataset Distribution by Language and Source",
        height=800 * n_rows,
        width=800 * n_cols,
        paper_bgcolor="#F7F7F7",   # light gray background
        plot_bgcolor="#676464",
        # uniformtext=dict(minsize=10, mode="hide"),
    )

    save_path = repo_path / "images" / "language_distribution.html"
    save_path_svg = repo_path / "images" / "language_distribution.svg"

    logger.info(f"Saving dataset language plot to {save_path} and {save_path_svg}.")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(save_path)
    fig.write_image(save_path_svg)