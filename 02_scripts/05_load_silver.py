from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql+psycopg2://asclepius_user:asclepius_password"
    "@localhost:5434/asclepius"
)

engine = create_engine(DATABASE_URL)

sql = """
TRUNCATE TABLE silver.clinical_notes;

INSERT INTO silver.clinical_notes (
    bronze_id,
    patient_id,
    note,
    question,
    answer,
    task,
    note_length,
    question_length,
    answer_length
)
SELECT
    id AS bronze_id,
    raw_record->>'patient_id' AS patient_id,
    raw_record->>'note' AS note,
    raw_record->>'question' AS question,
    raw_record->>'answer' AS answer,
    raw_record->>'task' AS task,
    LENGTH(raw_record->>'note') AS note_length,
    LENGTH(raw_record->>'question') AS question_length,
    LENGTH(raw_record->>'answer') AS answer_length
FROM bronze.clinical_notes_raw;
"""

with engine.begin() as conn:
    conn.execute(text(sql))

print("✓ Silver table loaded from Bronze.")