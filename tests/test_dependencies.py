import os.path
from unittest import TestCase

import tomli

HERE = os.path.dirname(os.path.realpath(__file__))
PYPROJECT_TOML = os.path.join(HERE, "..", "pyproject.toml")


class DependenciesTest(TestCase):
    def setUp(self) -> None:
        with open(PYPROJECT_TOML, "rb") as f:
            self.poetry_conf = tomli.load(f)["tool"]["poetry"]

    def test_required_dependencies(self):
        deps = self.poetry_conf["dependencies"].keys()
        self.assertCountEqual(
            ["python", "protobuf", "grpcio-tools"],
            deps,
        )

    def test_dev_dependencies(self):
        deps = self.poetry_conf["group"]["dev"]["dependencies"].keys()
        self.assertCountEqual(["pre-commit", "coverage", "tomli"], deps)
