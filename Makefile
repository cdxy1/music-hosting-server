.PHONY: lint, fmt

lint:
	uv run ruff check --fix

fmt: lint
	uv run ruff format .

