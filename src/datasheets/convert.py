import pandas as pd
from transformers import AutoTokenizer
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Tokenize text in a JSONL file and save to Parquet with token counts"
)
parser.add_argument("--input", type=str, required=True, help="Path to input JSONL file")
parser.add_argument(
    "--output", type=str, required=True, help="Path to output Parquet file"
)
args = parser.parse_args()

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("AI-Sweden-Models/Llama-3-8B-instruct")

# Read the JSONL file
df = pd.read_json(args.input, lines=True)

# Tokenize the 'text' column and count tokens
df["token_count"] = df["text"].apply(
    lambda x: len(tokenizer.encode(str(x), add_special_tokens=False))
)

df = df[df["token_count"] > 0]
# Save to a Parquet file with gzip compression
df.to_parquet(args.output, index=False, compression="gzip")
