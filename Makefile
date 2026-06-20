.PHONY: setup run-example

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run-example:
	.venv/bin/python 00_foundations/Examples/01_first_llm_call.py