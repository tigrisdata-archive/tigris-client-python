# tigris-client-python

Python client for Tigris

# Development

1. Install `poetry` following the installation instructions [here](https://python-poetry.org/docs/#installation)
2. Requires **python 3.7+**, **pip 23.x**
3. Clone the repo and cd into the directory
4. Update submodule - `git submodule update --init`
5. Create and activate the virtual environment - `poetry shell`
6. Install dependencies - `poetry install --with dev`
7. Compile proto and generate api client helpers - `make generate`

### Usage
See reference implementation in `./tests` directory that uses Tigris on `localhost:8081`
