name := 01_basic.py

run:
	uv run $(name)


lint:
	#uv run mypy --install-types
	@uvx ruff format
	@uvx ruff check --fix --select I
	@uv run mypy . # uvx runs in separate virtual environment.
