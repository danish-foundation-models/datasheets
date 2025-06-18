import argparse
import gzip
import json
import os
from multiprocessing import Pool, cpu_count
from typing import Any, Dict, List, Optional

import polars as pl
from tqdm import tqdm
from transformers import AutoTokenizer
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast

# --- Constants ---
MODEL_NAME = "AI-Sweden-Models/Llama-3-8B-instruct"
PARQUET_COMPRESSION = "zstd"

# --- Globals for Multiprocessing ---
# This global variable will be populated by the pool initializer in each worker process.
# This is a standard pattern to avoid pickling large objects like tokenizers.
_worker_tokenizer: Optional[PreTrainedTokenizerFast] = None


# --- Multiprocessing Functions ---


def initialize_worker_tokenizer() -> None:
    """
    Initializes the tokenizer for a single worker process.
    This function is called once per process in the multiprocessing pool.
    """
    global _worker_tokenizer
    _worker_tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME, use_fast=True, local_files_only=True
    )


def count_tokens_in_worker(text: str) -> int:
    """
    Counts tokens for a given text using the worker's initialized tokenizer.

    Args:
        text: The input string to tokenize.

    Returns:
        The number of tokens.

    Raises:
        RuntimeError: If the tokenizer is not initialized in the worker process.
    """
    if _worker_tokenizer is None:
        raise RuntimeError("Tokenizer not initialized in worker process.")
    return len(_worker_tokenizer.encode(str(text), add_special_tokens=False))


# --- Core Logic Functions ---


def process_batch(batch_of_texts: List[str]) -> List[int]:
    """
    Processes a batch of texts in parallel to count tokens for each.

    Args:
        batch_of_texts: A list of strings to process.

    Returns:
        A list of token counts corresponding to the input texts.
    """
    num_processes = cpu_count()
    # The initializer will call `initialize_worker_tokenizer` in each worker process
    with Pool(processes=num_processes, initializer=initialize_worker_tokenizer) as pool:
        return pool.map(count_tokens_in_worker, batch_of_texts)


def process_and_save_chunk(
    batch_of_dicts: List[Dict[str, Any]], output_dir: str, file_index: int
) -> Optional[str]:
    """
    Processes a batch of data, calculates token counts, filters, creates a
    DataFrame, and saves it as a Parquet chunk.

    Args:
        batch_of_dicts: A list of dictionaries, each expected to have a "text" key.
        output_dir: The directory to save the Parquet chunk file.
        file_index: The index for naming the chunk file.

    Returns:
        The path to the saved chunk file, or None if no data was saved.
    """
    if not batch_of_dicts:
        return None

    texts = [row["text"] for row in batch_of_dicts]
    token_counts = process_batch(texts)

    # Combine original data with token counts, filtering out empty texts
    rows_with_token_counts = [
        {**row, "token_count": token_count}
        for row, token_count in zip(batch_of_dicts, token_counts)
        if token_count > 0
    ]

    if not rows_with_token_counts:
        return None

    df = pl.DataFrame(rows_with_token_counts)
    chunk_path = os.path.join(output_dir, f"chunk_{file_index:04d}.parquet")
    df.write_parquet(chunk_path, compression=PARQUET_COMPRESSION)
    print(f"✓ Saved chunk {file_index} with {len(df)} rows to {chunk_path}")
    return chunk_path


def process_file_in_chunks(
    input_path: str, output_dir: str, batch_size: int
) -> List[str]:
    """
    Reads the input file, processes it in chunks, and saves intermediate Parquet files.

    Args:
        input_path: Path to the gzipped JSONL input file.
        output_dir: Directory to store intermediate chunk files.
        batch_size: The number of lines to process in each batch.

    Returns:
        A list of paths to the created chunk files.
    """
    chunk_files: List[str] = []
    batch: List[Dict[str, Any]] = []
    file_index = 0

    with gzip.open(input_path, "rt", encoding="utf-8") as infile:
        for line in tqdm(infile, desc="Reading & Processing Chunks"):
            batch.append(json.loads(line))
            if len(batch) >= batch_size:
                chunk_path = process_and_save_chunk(batch, output_dir, file_index)
                if chunk_path:
                    chunk_files.append(chunk_path)
                batch = []
                file_index += 1

    # Process the final partial batch
    if batch:
        chunk_path = process_and_save_chunk(batch, output_dir, file_index)
        if chunk_path:
            chunk_files.append(chunk_path)

    return chunk_files


def combine_chunks_and_cleanup(
    chunk_files: List[str], output_dir: str, final_filename: str
) -> None:
    """
    Combines all Parquet chunks into a single file and deletes the chunks.

    Args:
        chunk_files: A list of paths to the Parquet chunk files.
        output_dir: The directory where the final file will be saved.
        final_filename: The name for the final combined Parquet file.
    """
    if not chunk_files:
        print("No data was processed, no final file created.")
        return

    print(f"Combining {len(chunk_files)} chunk files...")
    # Lazily scan and collect to be more memory efficient for many files
    final_df = pl.concat(
        [pl.scan_parquet(p) for p in chunk_files], how="vertical"
    ).collect()

    final_output_path = os.path.join(output_dir, final_filename)
    final_df.write_parquet(final_output_path, compression=PARQUET_COMPRESSION)
    print(f"✓ Final DataFrame with {len(final_df)} rows saved to {final_output_path}")

    print("Cleaning up temporary chunk files...")
    for path in chunk_files:
        try:
            os.remove(path)
        except OSError as e:
            print(f"Error removing file {path}: {e}")
    print("✓ Cleanup complete.")


# --- Main Execution ---


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Process a large JSONL file, count tokens, and save as Parquet."
    )
    parser.add_argument(
        "--input", type=str, required=True, help="Path to the input gzipped JSONL file."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory to store intermediate and final output files.",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="Filename for the final combined Parquet file.",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=10000,
        help="Number of lines to process in each batch.",
    )
    return parser.parse_args()


def main() -> None:
    """Main function to orchestrate the script execution."""
    args = parse_arguments()

    os.makedirs(args.output_dir, exist_ok=True)

    chunk_files = process_file_in_chunks(
        input_path=args.input,
        output_dir=args.output_dir,
        batch_size=args.batch_size,
    )

    combine_chunks_and_cleanup(
        chunk_files=chunk_files,
        output_dir=args.output_dir,
        final_filename=args.output_file,
    )


if __name__ == "__main__":
    main()
