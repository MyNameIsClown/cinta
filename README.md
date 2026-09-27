# Cinta

CLI tool to auto-generate pipeline configuration for GitLab and GitHub.

> **Status:** early scaffold. The `cinta` command currently exists as a stub
> and does not yet generate real pipeline configs.

## Requirements

- Python >= 3.12

## Installation

```bash
pip install cinta
```

Or with [pipx](https://pipx.pypa.io/) for an isolated global install:

```bash
pipx install cinta
```

## Usage

```bash
cinta
```

## Project layout

```
src/cinta/
├── cli.py          # Typer app entrypoint (registers commands)
├── __main__.py      # `python -m cinta` entrypoint
└── app/
    └── main.py       # command implementations (generate_pipe, ...)
```

## Development

This project uses [Poetry](https://python-poetry.org/) internally to manage
dev dependencies and builds.

```bash
poetry install
poetry run cinta
```

## License

MIT
