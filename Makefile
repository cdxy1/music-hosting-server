.PHONY: lint, fmt, run, run-debug

lint:
	uv run ruff check --fix

fmt: lint
	uv run ruff format .

up:
	docker compose up -d

down:
	docker compose down

run:
	PYTHONPATH=. uv run src/setup/bootstrap.py

run-debug:
	uv run uvicorn src.setup.composition_root:app --reload
