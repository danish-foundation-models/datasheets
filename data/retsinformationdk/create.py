# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "datasets==3.2.0",
#     "pandas",
#     "requests",
#     "trafilatura",
#     "dynaword"
# ]
# [tool.uv.sources]
# dynaword = { git = "https://huggingface.co/datasets/danish-foundation-models/danish-dynaword", rev = "00e7f2aee7f7ad2da423419f77ecbb9c0536de0d" }
# ///

from datetime import date, datetime
from io import StringIO
import logging
from pathlib import Path
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from trafilatura import extract
from datasets import Dataset
from tqdm import tqdm

from dynaword.process_dataset import (
    add_token_count,
    ensure_column_order,
    remove_duplicate_text,
    remove_empty_texts,
)

TMP_DIR = Path(__file__).parent / "tmp"

BASE_URL = "https://www.retsinformation.dk/api/document/eli"

logger = logging.getLogger(__name__)
today = date.today()


def create_session_with_retries(retries=2, backoff_factor=0.5):
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def fetch_document_list():
    download = True
    csv_content = ""

    df: pd.DataFrame = pd.DataFrame()

    if TMP_DIR.exists():
        files = list(TMP_DIR.glob("*.csv"))
        file = sorted(files, reverse=True)[0]

        file_date = datetime.strptime(file.stem, "%Y-%m-%d").date()

        if (today - file_date).days < 180:
            download = False
            df = pd.read_csv(file)

    if download:
        logger.info("Downloading list of files from Retsinformation.dk")
        response = requests.get(
            "https://www.retsinformation.dk/api/documentsearch/csv?dt=10&dt=1480&dt=20&dt=30&dt=40&dt=50&dt=90&dt=120&dt=270&dt=60&dt=100&dt=80&dt=110&dt=130&dt=140&dt=150&dt=160&dt=170&dt=180&dt=200&dt=210&dt=220&dt=1510&dt=1490&dt=-10&dt=230&dt=240&dt=250&dt=260&dt=980&dt=360&dt=400&dt=380&dt=420&dt=1530&dt=440&dt=450&dt=430&dt=1540&dt=460&dt=410&dt=370&dt=480&dt=390&dt=500&dt=510&dt=520&dt=490&dt=300&dt=310&dt=320&dt=330&dt=340&dt=350&o=40"
        )
        # response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses

        # The response is a gzip-compressed CSV in plain text
        csv_content = response.content.decode("utf-16", errors="replace")
        logger.info("Downloaded list of documents")

        # Optionally parse with pandas
        df = pd.read_csv(StringIO(csv_content), sep=";")  # Assuming semicolon separator

        df.to_csv(TMP_DIR / (today.strftime("%Y-%m-%d") + ".csv"), index=False)

    return df[
        [
            "DokumentType",
            "DokumentId",
            "Titel",
            "Ressort",
            "Historisk",
            "PubliceretTidspunkt",
            "EliUrl",
        ]
    ]


def fetch_document(doc_info: pd.Series, session: requests.Session) -> dict:
    url = BASE_URL + doc_info["EliUrl"].strip().split("eli")[1]

    response = session.post(
        url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        json={},
    )
    response.raise_for_status()

    return response.json()[0]


def main():
    save_path = Path(__file__).parent / "retsinformationdk.parquet"
    documents = fetch_document_list()

    logger.info(f"Found {len(documents)} documents from retsinformationdk")

    session = create_session_with_retries()
    docs = []
    for idx, doc_info in tqdm(documents.iterrows(), total=len(documents)):
        if doc_info["Historisk"]:
            continue
        try:
            doc = fetch_document(doc_info, session)
            text = extract(doc["documentHtml"], output_format="markdown")
            docs.append(
                {
                    "id": doc_info["DokumentId"],
                    "text": text if text else "",
                    "source": "retsinformationdk",
                    "added": today.strftime("%Y-%m-%d"),
                    "created": f"{date.fromisoformat(str(doc_info['PubliceretTidspunkt'])).strftime('%Y-%m-%d')}, {date.fromisoformat(str(doc_info['PubliceretTidspunkt'])).strftime('%Y-%m-%d')}",
                }
            )
        except Exception as e:
            logger.error(f"Ran in to error: {e}")
            logger.error(f"Skipping doc {doc_info['DokumentId']}")

    ds = Dataset.from_list(docs)

    # quality checks and processing
    ds = remove_empty_texts(ds)
    ds = remove_duplicate_text(ds)
    ds = add_token_count(ds)
    ds = ensure_column_order(ds)

    ds.to_parquet(save_path)


if __name__ == "__main__":
    log_path = Path(__file__).parent / "retsinformationdk.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path),
        ],
    )
    main()
