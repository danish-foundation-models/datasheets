#!/bin/bash

# Define desired dataset
DATASET_NAME=$1

# Define input and output directories
INPUT_DIR="$2/$DATASET_NAME/documents" # /path/up/to/{dataset_name} - but without dataset name
OUTPUT_DIR="$3/$DATASET_NAME/original/v1.0.0" # /path/up/to/{dataset_name} - but without dataset name

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Loop through all .jsonl.gz files in the input directory
for file in $INPUT_DIR/*.jsonl.gz; do
    # Check if any files were found
    if [[ -f "$file" ]]; then
        # Extract the base name (without path and .jsonl.gz extension)
        basename=$(basename "$file" .jsonl.gz)
        # Define output file path
        output_file=$OUTPUT_DIR/$basename.parquet
        # Run the Python script
        uv run src/datasheets/convert.py --input "$file" --output "$output_file"
        echo "Processed $file -> $output_file"
    else
        echo "No .jsonl.gz files found in $INPUT_DIR"
        exit 1
    fi
done

# Add datasheet directory
mkdir -p data/$DATASET_NAME/
cp template/template.md data/$DATASET_NAME/$DATASET_NAME.md

# Run statistics
uv run src/datasheets/update_descriptive_statistics.py --dataset $DATASET_NAME