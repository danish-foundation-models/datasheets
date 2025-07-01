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

from datetime import datetime
import gc
import logging
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datasets import Dataset, load_dataset
import pandas as pd
from tqdm import tqdm
import pyarrow as pa
import pyarrow.parquet as pq

from dynaword.process_dataset import (
    add_token_count,
    ensure_column_order,
    remove_duplicate_text,
    remove_empty_texts,
)

SOURCE = "cvr-reports"

ROW_TEMPLATE = {
    "id": "",
    "source": SOURCE,
    "added": datetime.today().date().strftime("%Y-%m-%d"),
    "created": f"2010-01-01, {datetime.today().date().strftime('%Y-%m-%d')}",
    "text": "",
}


logger = logging.getLogger(__name__)


def get_md_files(input_dir: Path, max_size: int | None = None) -> list[Path]:
    md_files = []

    for subdir in tqdm(input_dir.iterdir(), desc="Scanning folders"):
        md_file = subdir / f"{subdir.name}.md"
        if md_file.exists():
            md_files.append(md_file)
            if max_size is not None and len(md_files) >= max_size:
                break

    return md_files


def read_file(md_file: Path) -> dict:
    row = ROW_TEMPLATE.copy()
    row["id"] = md_file.stem
    row["text"] = md_file.read_text(encoding="utf-8")
    return row


def main(input_dir: Path, save_path: Path):
    # if not save_path.name.endswith(".parquet"):
    #     save_path.mkdir(parents=True)
    #     save_path = save_path / f"{SOURCE}.parquet"

    # logger.info("Scanning files...")
    # md_files = get_md_files(input_dir, max_size=None)
    # logger.info(f"Found {len(md_files)} files.")

    # with ThreadPoolExecutor() as executor:
    #     rows = list(
    #         tqdm(
    #             executor.map(read_file, md_files),
    #             total=len(md_files),
    #             desc="Reading files",
    #         )
    #     )

    # logger.info("Converting rows to dataframe")
    # df = pd.DataFrame(rows)
    # logger.info("Converting dataframe to table")
    # table: pa.Table = pa.Table.from_pandas(df)
    # logger.info("Converting table to dataset")

    # # Save directly to Parquet
    # pq.write_table(table, str(save_path))
    # del table
    # gc.collect()
    new_save_path = save_path.parent / (save_path.stem + "_processed.parquet")
    print(new_save_path)

    ds = load_dataset(
        path="parquet", data_files=[str(save_path)], split="train", num_proc=15
    )
    ds = remove_empty_texts(ds, num_proc=15)  # type: ignore
    ds = remove_duplicate_text(ds)
    ds = add_token_count(ds, num_proc=10)
    ds = ensure_column_order(ds)

    ds.to_parquet(str(new_save_path))


if __name__ == "__main__":
    input_path = Path(sys.argv[1])
    save_path = Path(sys.argv[2])
    log_path = Path(__file__).parent / f"{SOURCE}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path),
        ],
    )
    main(input_path, save_path)
