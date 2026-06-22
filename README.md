## Running the Examples

This repository contains independent examples designed to demonstrate different Artificial Intelligence concepts.

## Environment Variables

Before running any example, create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY='sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx'
```

### Verify Configuration

You can verify that the API key is being loaded correctly by running:

```bash
make run-example
```

If the API key is not configured correctly, you should see an error similar to:

```text
OPENAI_API_KEY not found. Check if the .env file exists in the project root.
```

### Security Notes

* Never commit your `.env` file to Git.
* Never share your API key publicly.
* Ensure `.env` is included in `.gitignore`.

Example `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```


### Option 1 – Run Examples Individually

Navigate to the desired example folder and execute the Python script.

Example:

```bash
cd Examples
python 01_first_llm_call.py
```

This approach is useful when exploring examples one at a time.

---

### Option 2 – Use Make Commands

The repository provides a Makefile to simplify setup and execution.

Install dependencies:

```bash
make install
```

Run the first example:

```bash
make run-example
```

Using Make commands is recommended because it provides a consistent execution process across all examples.

---

### Environment Variables

Before running any example, create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

The examples will automatically load the API key from this file.

---

### Recommended Workflow

1. Clone the repository.
2. Create a `.env` file.
3. Run:

```bash
make install
```

4. Execute examples using either:

```bash
python <example_file>.py
```

or

```bash
make <target>
```
### Troubleshooting

If an example fails:

1. Verify that Python is installed.
2. Verify that dependencies were installed.
3. Verify that the `.env` file exists.
4. Verify that the API key is valid.

# PROJECT

Overview

This project provides a local environment for experimenting with synthetic healthcare datasets, vector databases, Retrieval-Augmented Generation (RAG), and AI evaluation methodologies.

The initial dataset used in this project is the Asclepius Synthetic Clinical Notes dataset from Hugging Face. Because the data is synthetic, it can be used for research, experimentation, and reproducible AI evaluations without exposing real patient information.

The environment includes:

PostgreSQL 16
pgvector extension for vector embeddings and semantic search
pgAdmin for database administration
Python scripts for dataset ingestion
Future support for embeddings, RAG pipelines, and evaluation frameworks

The primary goal is to create a reproducible AI engineering laboratory focused on healthcare use cases and LLM evaluation.

Architecture
Asclepius Dataset
        │
        ▼
    PostgreSQL
    + pgvector
        │
        ▼
   Embeddings
        │
        ▼
   Vector Search
        │
        ▼
       RAG
        │
        ▼
      Evals

Requirements
Docker Desktop
Python 3.9+
Make
Git
Starting the Environment

Start PostgreSQL and pgAdmin:

make up

Initialize pgvector:

make db-init

Verify the extension:

make db-check
Database Access
PostgreSQL

Connection details:

Host: localhost
Port: 5434
Database: asclepius
User: asclepius_user
Password: asclepius_password
pgAdmin

Open:

http://localhost:5051

Credentials:

Email: admin@local.com
Password: admin

When registering the server inside pgAdmin:

Host: postgres
Port: 5432
Database: asclepius
User: asclepius_user
Password: asclepius_password
Recommended Tool: DBeaver

Although pgAdmin is included in this project, DBeaver is recommended for day-to-day development and data exploration.
Download DBeaver -> DBeaver Community Edition (https://chatgpt.com/c/6a36bbaa-31e4-83e9-baab-baa9c6d36b51#:~:text=DBeaver%20Community%20Edition)

Benefits:

Better SQL editor experience
Query history
Export and import tools
Schema navigation
Data profiling
Works with PostgreSQL, Databricks, SQL Server, MySQL, Snowflake, and many other databases

Connection settings in DBeaver:

Host: localhost
Port: 5434
Database: asclepius
User: asclepius_user
Password: asclepius_password
Useful Commands

Start services:

make up

Stop services:

make down

View logs:

make logs

Open PostgreSQL shell:

make db-shell

Load a sample dataset:

make load-sample

Load the full dataset:

make load-full

Count records:

make count