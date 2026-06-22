from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql+psycopg2://asclepius_user:asclepius_password"
    "@localhost:5434/asclepius"
)

engine = create_engine(DATABASE_URL)

sql = """
CREATE SCHEMA IF NOT EXISTS silver;

CREATE TABLE IF NOT EXISTS silver.clinical_notes (
    id BIGSERIAL PRIMARY KEY,
    bronze_id BIGINT,
    patient_id TEXT,
    note TEXT,
    question TEXT,
    answer TEXT,
    task TEXT,
    note_length INTEGER,
    question_length INTEGER,
    answer_length INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

with engine.begin() as conn:
    conn.execute(text(sql))

print("✓ Silver schema and table created.")