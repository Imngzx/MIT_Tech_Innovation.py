# Setup, Development & Building For This Project

- Libraries installation:
  1. Declare the lib name inside the `pyproject.toml`
  2. run `uv sync` to install all the libraries

- Preferred tools:
  - `uv` for project management
  - `ty` or `pyrefly` as LSP
  - `ruff` as formatter and linter

| Task | Commands |
| -------------- | --------------- |
| `uv sync` | install all the dependiencies/libs |
| `uv run python -m src.main` | run the code |
