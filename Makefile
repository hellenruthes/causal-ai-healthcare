.PHONY: setup run-example

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run-example:
	.venv/bin/python 00_foundations/Examples/01_first_llm_call.py

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker ps

db-shell:
	docker exec -it asclepius_postgres psql -U asclepius_user -d asclepius

db-init:
	docker exec -it asclepius_postgres psql -U asclepius_user -d asclepius -c "CREATE EXTENSION IF NOT EXISTS vector;"

load-sample:
	python scripts/load_asclepius.py --sample 100

load-full:
	python scripts/load_asclepius.py

count:
	docker exec -it asclepius_postgres psql -U asclepius_user -d asclepius -c "SELECT COUNT(*) FROM clinical_notes;"

download-sample:
	python3 02_scripts/01_download_asclepius.py --sample 100

download-full:
	python3 02_scripts/01_download_asclepius.py

make pipeline-sample