import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

import grpc

from tigrisdb.client import TigrisClient
from tigrisdb.types import ClientConfig


@patch("grpc.channel_ready_future")
class TigrisClientTest(TestCase):
    def setUp(self) -> None:
        self.done_future = MagicMock(grpc.Future)

    def test_without_config(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient()
        self.assertEqual("localhost:8081", client.config.server_url)
        self.assertIsNone(client.config.client_id)
        self.assertIsNone(client.config.client_secret)
        self.assertIsNone(client.config.project_name)
        self.assertEqual("", client.config.branch)

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
    def test_with_config(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(
            config=ClientConfig(
                server_url="test_url",
                project_name="test_project",
                client_id="test_client_id",
                client_secret="test_client_secret",
                branch="test_branch",
            )
        )
        self.assertEqual("test_url:443", client.config.server_url)
        self.assertEqual("test_client_id", client.config.client_id)
        self.assertEqual("test_client_secret", client.config.client_secret)
        self.assertEqual("test_project", client.config.project_name)
        self.assertEqual("test_branch", client.config.branch)

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
    def test_with_env_vars(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient()
        self.assertEqual("uri_env:443", client.config.server_url)
        self.assertEqual("client_env", client.config.client_id)
        self.assertEqual("secret_env", client.config.client_secret)
        self.assertEqual("project_env", client.config.project_name)
        self.assertEqual("branch_env", client.config.branch)

    def test_strip_https(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(config=ClientConfig(server_url="https://my.tigris.dev"))
        self.assertEqual("my.tigris.dev:443", client.config.server_url)
        client = TigrisClient(config=ClientConfig(server_url="http://my.tigris.dev"))
        self.assertEqual("my.tigris.dev:443", client.config.server_url)

    def test_get_db(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient()
        self.assertEqual(client.config.branch, client.get_db().branch)
        self.assertEqual(client.config.project_name, client.get_db().project)

    def test_get_search(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient()
        self.assertEqual(client.config.project_name, client.get_search().project)
