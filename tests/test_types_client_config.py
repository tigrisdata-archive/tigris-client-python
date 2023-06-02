import os
from unittest import TestCase
from unittest.mock import patch

from tigrisdb.types import ClientConfig


class ClientConfigTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_init_with_none(self):
        conf = ClientConfig()
        self.assertIsNone(conf.project_name)
        self.assertEqual(conf.server_url, "api.preview.tigrisdata.cloud")
        self.assertIsNone(conf.client_id)
        self.assertIsNone(conf.client_secret)
        self.assertEqual(conf.branch, "")

    @patch.dict(
        os.environ,
        {
            "TIGRIS_URI": "uri_env",
            "TIGRIS_PROJECT": "project_env",
            "TIGRIS_CLIENT_ID": "client_env",
            "TIGRIS_CLIENT_SECRET": "secret_env",
            "TIGRIS_DB_BRANCH": "branch_env",
        },
    )
    def test_init_with_all_args(self):
        conf = ClientConfig(
            server_url="uri",
            project_name="project",
            client_id="client",
            client_secret="secret",
            branch="branch",
        )
        self.assertEqual(conf.server_url, "uri")
        self.assertEqual(conf.project_name, "project")
        self.assertEqual(conf.client_id, "client")
        self.assertEqual(conf.client_secret, "secret")
        self.assertEqual(conf.branch, "branch")

    @patch.dict(
        os.environ,
        {
            "TIGRIS_URI": "uri_env",
            "TIGRIS_PROJECT": "project_env",
            "TIGRIS_CLIENT_ID": "client_env",
            "TIGRIS_CLIENT_SECRET": "secret_env",
            "TIGRIS_DB_BRANCH": "branch_env",
        },
    )
    def test_init_with_all_env(self):
        conf = ClientConfig()
        self.assertEqual(conf.server_url, "uri_env")
        self.assertEqual(conf.project_name, "project_env")
        self.assertEqual(conf.client_id, "client_env")
        self.assertEqual(conf.client_secret, "secret_env")
        self.assertEqual(conf.branch, "branch_env")

    @patch.dict(
        os.environ,
        {
            "TIGRIS_CLIENT_ID": "client_env",
            "TIGRIS_DB_BRANCH": "branch_env",
        },
    )
    def test_init_with_partial_env(self):
        conf = ClientConfig(project_name="project")
        self.assertEqual(conf.project_name, "project")
        self.assertEqual(conf.client_id, "client_env")
        self.assertIsNone(conf.client_secret)
        self.assertEqual(conf.branch, "branch_env")

    def test_validate_without_project(self):
        conf = ClientConfig()
        with self.assertRaisesRegex(
            ValueError, "`TIGRIS_PROJECT` environment variable"
        ):
            conf.validate()

    def test_validate_without_client_id(self):
        conf = ClientConfig(project_name="project")
        conf.validate()
        with self.assertRaisesRegex(
            ValueError, "`TIGRIS_CLIENT_ID` environment variable"
        ):
            conf.validate(True)

    def test_validate_without_client_secret(self):
        conf = ClientConfig(project_name="project", client_id="id")
        conf.validate()
        with self.assertRaisesRegex(
            ValueError, "`TIGRIS_CLIENT_SECRET` environment variable"
        ):
            conf.validate(True)

    def test_validate_no_error(self):
        conf = ClientConfig(
            project_name="project", client_id="id", client_secret="secret"
        )
        conf.validate()
        conf.validate(True)
