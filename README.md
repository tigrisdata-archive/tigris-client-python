# tigris-client-python
Python client for Tigris

# Development
1. Requires **python 3.7+**, **pip 23.x**
2. Clone the repo and cd into the directory
3. Update submodule - `git submodule --init`
4. Install virtualenv - `pip install virtualenv`
5. Create virtualenv in the project directory - `virtualenv venv`
6. Activate virtualenv - `. venv/bin/activate`
7. Install dependencies - `pip install -r requirements.txt`
8. Compile proto and generate api client helpers - `make generate`