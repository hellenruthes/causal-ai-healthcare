import json
from pathlib import Path

from sqlalchemy import create_engine, text

DATA_FILE = Path(
    "03_data/raw_data/asclepius_clinical_notes_sample_100.json"
)

DATABASE_URL = (
    "postgresql+psycopg2://asclepius_user:asclepius_password"
    "@localhost:5434/asclepius"
)

engine = create_engine(DATABASE_URL)

print(f"Reading {DATA_FILE}...")

with open(DATA_FILE, "r") as f:
    records = [json.loads(line) for line in f]

print(f"Found {len(records)} records")

with engine.begin() as conn:

    for record in records:

        conn.execute(
            text(
                """
                INSERT INTO bronze.clinical_notes_raw (
                    raw_record
                )
                VALUES (
                    CAST(:record AS JSONB)
                )
                """
            ),
            {
                "record": json.dumps(record)
            }
        )

print(f"✓ Loaded {len(records)} records into bronze.clinical_notes_raw")