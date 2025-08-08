import logging
from pathlib import Path
from typing import cast

import pandas as pd
import plotnine as pn
from datasets import Dataset

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
