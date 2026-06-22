from pathlib import Path
from datasets import load_dataset
import argparse

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "03_data" / "raw_data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser()

parser.add_argument(
    "--sample",
    type=int,
    default=None,
    help="Number of records to download"
)

args = parser.parse_args()

split = f"train[:{args.sample}]" if args.sample else "train"
suffix = f"sample_{args.sample}" if args.sample else "full"

print(f"Loading {split}...")

ds = load_dataset(
    "starmpcc/Asclepius-Synthetic-Clinical-Notes",
    split=split
)

print(ds)
print(f"Columns: {ds.column_names}")

output_file = DATA_DIR / f"asclepius_clinical_notes_{suffix}.json"

ds.to_json(str(output_file))

print(f"✓ Saved to: {output_file}")
print(f"✓ Rows: {len(ds)}")
print(f"✓ File size: {output_file.stat().st_size / 1024 / 1024:.2f} MB")