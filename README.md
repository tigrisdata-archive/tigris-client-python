# tigris-client-python

Python client for Tigris

## Installation

```commandline
pip install tigrisdb
```

# Usage

See reference implementation in `./tests` directory that uses Tigris on `localhost:8081`

# Development

1. Install `poetry` following the installation instructions [here](https://python-poetry.org/docs/#installation)
2. Requires **python 3.8+**, **pip 23.x**
3. Clone the repo and cd into the directory
4. Update submodule - `git submodule update --init`
5. Create and activate the virtual environment - `poetry shell`
6. Install dependencies - `poetry install --with dev`
7. [Optional] install [git hooks](#git-hooks)
8. Compile proto and generate api client helpers - `poetry run make generate`

## Git Hooks

We use [pre-commit](https://pre-commit.com/index.html) to automatically
setup and run git hooks.

On every `git commit` we check the code quality. Install the hooks:

```commandline
pre-commit install
```
