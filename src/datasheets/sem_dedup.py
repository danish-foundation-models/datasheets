#!/usr/bin/env python3
"""
Text deduplication script using SemHash for large datasets.
"""

import argparse
import logging
import sys
import time
import psutil
from pathlib import Path
from typing import cast, List

from datasets import load_dataset, Dataset
from semhash import SemHash
from semhash.datamodels import DeduplicationResult
from model2vec import StaticModel

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from datasheets.update_descriptive_statistics import find_latest_dataset_version
from datasheets.paths import repo_path


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Setup logging configuration."""
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("deduplication.log"),
        ],
    )
    return logging.getLogger(__name__)


def log_memory_usage(logger: logging.Logger, step: str) -> None:
    """Log current memory usage."""
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / 1024 / 1024
    logger.info(f"Memory usage at {step}: {memory_mb:.2f} MB")


def get_dataset_path(dataset_name: str, logger: logging.Logger) -> Path:
    """
    Get the path to the latest version of a dataset.

    Args:
        dataset_name: Name of the dataset
        logger: Logger instance

    Returns:
        Path to the dataset

    Raises:
        FileNotFoundError: If dataset doesn't exist
        RuntimeError: If no valid dataset version found
    """
    logger.info(f"Looking for dataset: {dataset_name}")

    try:
        dataset_data_path = repo_path.parent / "datasets" / dataset_name
        logger.debug(f"Dataset search path: {dataset_data_path}")

        if not dataset_data_path.exists():
            raise FileNotFoundError(f"Dataset directory not found: {dataset_data_path}")

        latest_version_dataset_path = find_latest_dataset_version(dataset_data_path)

        if not latest_version_dataset_path:
            raise RuntimeError(f"No valid dataset version found for: {dataset_name}")

        logger.info(f"Found dataset at: {latest_version_dataset_path}")
        return latest_version_dataset_path

    except Exception as e:
        logger.error(f"Error finding dataset {dataset_name}: {e}")
        raise


def load_model(model_name: str, logger: logging.Logger) -> StaticModel:
    """
    Load the specified model.

    Args:
        model_name: Name/path of the model to load
        logger: Logger instance

    Returns:
        Loaded StaticModel instance

    Raises:
        RuntimeError: If model loading fails
    """
    logger.info(f"Loading model: {model_name}")
    start_time = time.time()

    try:
        model = StaticModel.from_pretrained(model_name)
        load_time = time.time() - start_time
        logger.info(f"Model loaded successfully in {load_time:.2f} seconds")
        log_memory_usage(logger, "after model loading")
        return model

    except Exception as e:
        logger.error(f"Failed to load model {model_name}: {e}")
        raise RuntimeError(f"Model loading failed: {e}")


def load_dataset_from_path(
    dataset_path: Path, num_proc: int, logger: logging.Logger
) -> Dataset:
    """
    Load dataset from the specified path.

    Args:
        dataset_path: Path to the dataset
        num_proc: Number of processes for loading
        logger: Logger instance

    Returns:
        Loaded Dataset instance

    Raises:
        RuntimeError: If dataset loading fails
    """
    logger.info(f"Loading dataset from: {dataset_path}")
    logger.info(f"Using {num_proc} processes for dataset loading")
    start_time = time.time()

    try:
        ds = load_dataset(str(dataset_path.resolve()), split="train", num_proc=num_proc)
        ds = cast(Dataset, ds)

        load_time = time.time() - start_time
        logger.info(f"Dataset loaded successfully in {load_time:.2f} seconds")
        logger.info(f"Dataset size: {len(ds)} records")
        logger.info(f"Dataset columns: {ds.column_names}")
        log_memory_usage(logger, "after dataset loading")

        return ds

    except Exception as e:
        logger.error(f"Failed to load dataset from {dataset_path}: {e}")
        raise RuntimeError(f"Dataset loading failed: {e}")


def validate_columns(
    dataset: Dataset, columns: List[str], logger: logging.Logger
) -> None:
    """
    Validate that specified columns exist in the dataset.

    Args:
        dataset: The loaded dataset
        columns: List of column names to validate
        logger: Logger instance

    Raises:
        ValueError: If any column is missing
    """
    missing_columns = [col for col in columns if col not in dataset.column_names]
    if missing_columns:
        error_msg = f"Missing columns in dataset: {missing_columns}. Available columns: {dataset.column_names}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    logger.info(f"All specified columns found: {columns}")


def perform_deduplication(
    dataset: Dataset,
    model: StaticModel,
    columns: List[str],
    threshold: float,
    logger: logging.Logger,
) -> DeduplicationResult:
    """
    Perform deduplication on the dataset.

    Args:
        dataset: Dataset to deduplicate
        model: Model for computing embeddings
        columns: Columns to use for deduplication
        logger: Logger instance

    Returns:
        Deduplication results

    Raises:
        RuntimeError: If deduplication fails
    """
    logger.info("Starting deduplication process")
    logger.info(f"Deduplicating on columns: {columns}")
    start_time = time.time()

    try:
        # Initialize SemHash
        logger.info("Initializing SemHash...")
        semhash = SemHash.from_records(records=dataset, model=model, columns=columns)  # type: ignore
        log_memory_usage(logger, "after SemHash initialization")

        # Perform deduplication
        logger.info("Performing self-deduplication...")
        deduplicated_texts: DeduplicationResult = semhash.self_deduplicate(
            threshold=threshold
        )

        dedup_time = time.time() - start_time
        logger.info(f"Deduplication completed in {dedup_time:.2f} seconds")

        # Log statistics
        original_count = len(dataset)
        deduplicated_count = len(deduplicated_texts.selected)
        removed_count = original_count - deduplicated_count
        removal_percentage = (
            (removed_count / original_count) * 100 if original_count > 0 else 0
        )

        logger.info("Deduplication statistics:")
        logger.info(f"  Original records: {original_count:,}")
        logger.info(f"  Deduplicated records: {deduplicated_count:,}")
        logger.info(f"  Removed records: {removed_count:,}")
        logger.info(f"  Removal percentage: {removal_percentage:.2f}%")

        log_memory_usage(logger, "after deduplication")

        return deduplicated_texts

    except Exception as e:
        logger.error(f"Deduplication failed: {e}")
        raise RuntimeError(f"Deduplication process failed: {e}")


def save_results(
    deduplicated_texts: DeduplicationResult,
    output_path: Path,
    overwrite: bool,
    logger: logging.Logger,
) -> None:
    """
    Save deduplication results to parquet file.

    Args:
        deduplicated_texts: Results from deduplication
        output_path: Path to save the results
        overwrite: Whether to overwrite existing files
        logger: Logger instance

    Raises:
        FileExistsError: If output file exists and overwrite is False
        RuntimeError: If saving fails
    """
    logger.info(f"Saving results to: {output_path}")

    # Check if output file exists
    if output_path.exists() and not overwrite:
        error_msg = (
            f"Output file already exists: {output_path}. Use --overwrite to replace it."
        )
        logger.error(error_msg)
        raise FileExistsError(error_msg)

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    try:
        # Convert to DataFrame and save as parquet
        logger.info("Converting results to DataFrame...")
        df = pd.DataFrame(deduplicated_texts.selected)

        logger.info("Creating Arrow table...")
        table: pa.Table = pa.Table.from_pandas(df)

        logger.info("Writing parquet file...")
        pq.write_table(table, str(output_path))

        save_time = time.time() - start_time
        file_size_mb = output_path.stat().st_size / 1024 / 1024

        logger.info(f"Results saved successfully in {save_time:.2f} seconds")
        logger.info(f"Output file size: {file_size_mb:.2f} MB")
        log_memory_usage(logger, "after saving results")

    except Exception as e:
        logger.error(f"Failed to save results: {e}")
        raise RuntimeError(f"Saving failed: {e}")


def check_disk_space(output_path: Path, logger: logging.Logger) -> None:
    """
    Check if there's enough disk space for output.

    Args:
        output_path: Path where output will be saved
        logger: Logger instance

    Raises:
        RuntimeError: If insufficient disk space
    """
    try:
        disk_usage = psutil.disk_usage(str(output_path.parent))
        free_space_gb = disk_usage.free / 1024 / 1024 / 1024

        logger.info(f"Available disk space: {free_space_gb:.2f} GB")

        # Warn if less than 1GB free
        if free_space_gb < 1.0:
            logger.warning(
                f"Low disk space warning: only {free_space_gb:.2f} GB available"
            )

        # Error if less than 100MB free
        if free_space_gb < 0.1:
            raise RuntimeError(
                f"Insufficient disk space: only {free_space_gb:.2f} GB available"
            )

    except Exception as e:
        logger.warning(f"Could not check disk space: {e}")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Deduplicate text data using SemHash",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--dataset-name",
        type=str,
        required=True,
        help="Name of the dataset to deduplicate",
    )

    parser.add_argument(
        "--model-name",
        type=str,
        default="minishlab/potion-multilingual-128M",
        help="Name or path of the model to use for embeddings",
    )

    parser.add_argument(
        "--output-path",
        type=Path,
        help="Output path for deduplicated data (default: dataset_path/dataset_name.parquet.dedup)",
    )

    parser.add_argument(
        "--columns",
        type=str,
        nargs="+",
        default=["text"],
        help="Column names to use for deduplication",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=0.95,
        help="The threshold for which documents are being filtered",
    )

    parser.add_argument(
        "--num-proc",
        type=int,
        default=10,
        help="Number of processes for dataset loading",
    )

    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite output file if it exists"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level",
    )

    return parser.parse_args()


def main():
    """Main function."""
    args = parse_arguments()
    logger = setup_logging(args.log_level)

    logger.info("=" * 60)
    logger.info("Starting text deduplication process")
    logger.info("=" * 60)
    logger.info(f"Dataset: {args.dataset_name}")
    logger.info(f"Model: {args.model_name}")
    logger.info(f"Columns: {args.columns}")
    logger.info(f"Threshold: {args.threshold}")
    logger.info(f"Processes: {args.num_proc}")
    logger.info(f"Overwrite: {args.overwrite}")
    logger.info("=" * 60)

    total_start_time = time.time()

    try:
        # Get dataset path
        dataset_path = get_dataset_path(args.dataset_name, logger)

        # Set default output path if not provided
        if args.output_path is None:
            args.output_path = (
                dataset_path.parent.parent
                / "dedup"
                / dataset_path.parts[-1]
                / f"{args.dataset_name}.parquet"
            )
            if not args.output_path.parent.exists():
                args.output_path.parent.mkdir(parents=True)

        logger.info(f"Output path: {args.output_path}")

        # Check disk space
        check_disk_space(args.output_path, logger)

        # Load model
        model = load_model(args.model_name, logger)

        # Load dataset
        dataset = load_dataset_from_path(dataset_path, args.num_proc, logger)

        # Validate columns
        validate_columns(dataset, args.columns, logger)

        # Perform deduplication
        deduplicated_texts = perform_deduplication(
            dataset, model, args.columns, args.threshold, logger
        )

        # Save results
        save_results(deduplicated_texts, args.output_path, args.overwrite, logger)

        # Log total time
        total_time = time.time() - total_start_time
        logger.info("=" * 60)
        logger.info(f"Deduplication completed successfully in {total_time:.2f} seconds")
        logger.info(f"Output saved to: {args.output_path}")
        logger.info("=" * 60)

    except KeyboardInterrupt:
        logger.error("Process interrupted by user")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Process failed: {e}")
        logger.debug("Full traceback:", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
