#!/usr/bin/env python3
"""
Token-count a folder of parquet files without HuggingFace datasets.
Usage:
    python process_parquet_streaming.py <input_dir> <output_dir>
"""

from functools import partial
import sys
import datetime
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import logging

import pyarrow as pa
import pyarrow.parquet as pq
from transformers import AutoTokenizer

from dynaword.process_dataset import COLUMN_ORDER

# -------------------- configuration --------------------
TOKENIZER_NAME = "AI-Sweden-Models/Llama-3-8B-instruct"
BATCH_SIZE = 50_000
N_WORKERS = 4
# -------------------------------------------------------

# ---------- early logging setup ----------
# Force line buffering even inside nohup
if hasattr(sys.stdout, "fileno"):
    sys.stdout = open(
        sys.stdout.fileno(),
        mode="w",
        buffering=1,
        encoding=sys.stdout.encoding,
        closefd=False,
    )
if hasattr(sys.stderr, "fileno"):
    sys.stderr = open(
        sys.stderr.fileno(),
        mode="w",
        buffering=1,
        encoding=sys.stderr.encoding,
        closefd=False,
    )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME, use_fast=True)


# ---------- small helper ----------
def log(msg, ds_name):
    """Prefix every message with dataset name and flush."""
    logging.info(f"[{ds_name}] {msg}")


# ---------- token-count helper (Arrow → Arrow) ----------
def _token_lengths(texts: pa.StringArray) -> pa.IntegerArray:
    lengths = tokenizer(
        texts.to_pylist(),
        padding=False,
        truncation=False,
        return_length=True,
    )["length"]
    return pa.array(lengths, type=pa.int32())


# ---------- schema helpers ----------
def _build_target_schema(source_schema: pa.Schema) -> pa.Schema:
    """Build the final schema we want to write."""
    fields = list(source_schema)
    # add token_count if missing
    if "token_count" not in source_schema.names:
        fields.append(pa.field("token_count", pa.int32()))

    # add extra columns defined in COLUMN_ORDER
    for col in COLUMN_ORDER:
        if col in source_schema.names:
            continue
        if col in ("added", "created"):
            fields.append(pa.field(col, pa.string()))
        else:
            fields.append(pa.field(col, pa.string()))

    # respect COLUMN_ORDER
    ordered_fields = [f for name in COLUMN_ORDER for f in fields if f.name == name]
    return pa.schema(ordered_fields)


def _transform_table(table: pa.Table, target_schema: pa.Schema) -> pa.Table:
    """Add token_count + missing columns and reorder."""
    # token count
    if "token_count" not in table.column_names:
        token_counts = _token_lengths(table["text"])
        table = table.append_column("token_count", token_counts)

    # missing columns
    n_rows = len(table)
    for col in COLUMN_ORDER:
        if col not in table.column_names:
            if col in ("added", "created"):
                col_data = pa.array([datetime.datetime.today().isoformat()] * n_rows)
            else:
                col_data = pa.array([""] * n_rows)
            table = table.append_column(col, col_data)

    # enforce order
    table = table.select(target_schema.names)
    return table.cast(target_schema)  # ensure exact dtypes


# ---------- file-level worker ----------
def process_one_file(parquet: Path, out_path: Path) -> None:
    ds_name = parquet.stem
    try:
        _real_process_one_file(parquet, out_path, ds_name)
    except Exception as e:
        log(f"[ERROR] {type(e).__name__}: {e}", ds_name)
        raise  # let ProcessPoolExecutor propagate it (optional)


def _real_process_one_file(parquet: Path, out_path: Path, ds_name: str) -> None:
    output_path = out_path / ds_name / "original" / "v1.0.0"
    output_file = output_path / f"{ds_name}.parquet"

    if output_file.exists():
        log("already processed – skipping", ds_name)
        return

    # if ds_name.startswith("uspto_filtered"):
    #     log("filtered dataset – skipping", ds_name)
    #     return

    log("loading …", ds_name)
    source_file = pq.ParquetFile(parquet)

    first_batch = next(source_file.iter_batches(batch_size=1))
    src_schema = pa.Table.from_batches([first_batch]).schema
    target_schema = _build_target_schema(src_schema)

    output_path.mkdir(parents=True, exist_ok=True)
    total_rows = 0

    with pq.ParquetWriter(output_file, schema=target_schema) as writer:
        for idx, batch in enumerate(source_file.iter_batches(batch_size=BATCH_SIZE)):
            log(f"processing batch {idx} ({len(batch)} rows)", ds_name)
            table = pa.Table.from_batches([batch])
            table = _transform_table(table, target_schema)
            writer.write_table(table)
            total_rows += len(batch)

    log(f"finished – wrote {total_rows} rows to {output_file}", ds_name)


# ---------- main entry ----------
def main(in_path: Path, out_path: Path) -> None:
    files = sorted(in_path.glob("*.parquet"))
    if not files:
        logging.warning("No .parquet files found in %s", in_path)
        return

    with ProcessPoolExecutor(max_workers=N_WORKERS) as ex:
        ex.map(partial(process_one_file, out_path=out_path), files)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python process_parquet_streaming.py <input_dir> <output_dir>")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
