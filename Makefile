run:
	uv run $(name)


lint:
	#uv run mypy --install-types
	@uv run ruff format
	@uv run ruff check --fix --select I
	@uv run mypy . # uvx runs in separate virtual environment.
