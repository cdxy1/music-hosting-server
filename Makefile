.PHONY: lint, fmt, run, run-debug, migrate, upgrade

lint:
	uv run ruff check --fix

fmt: lint
	uv run ruff format .

up:
	docker compose up --build -d

down:
	docker compose down

run:
	PYTHONPATH=. uv run src/setup/bootstrap.py

run-debug:
	uv run uvicorn src.setup.composition_root:app --reload

migrate:
	uv run alembic revision --autogenerate -m "$(msg)"

upgrade:
	uv run alembic upgrade head
