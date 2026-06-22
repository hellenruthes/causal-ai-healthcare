from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql+psycopg2://asclepius_user:asclepius_password"
    "@localhost:5434/asclepius"
)

engine = create_engine(DATABASE_URL)

statements = [
    """
    CREATE SCHEMA IF NOT EXISTS bronze;
    """,
    """
    CREATE TABLE IF NOT EXISTS bronze.clinical_notes_raw (
        id BIGSERIAL PRIMARY KEY,
        raw_record JSONB NOT NULL,
        ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
]

with engine.begin() as conn:
    for stmt in statements:
        conn.execute(text(stmt))

print("✓ Bronze schema and table created.")