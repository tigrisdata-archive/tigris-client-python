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

    def test_init_with_none(self, ready_future):
        ready_future.return_value = self.done_future
        with self.assertRaisesRegex(
            ValueError, "`TIGRIS_PROJECT` environment variable"
        ):
            TigrisClient()

    def test_init_with_complete_dict(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(
            {
                "server_url": "uri",
                "project": "project",
                "client_id": "client",
                "client_secret": "secret",
                "branch": "branch",
            }
        )
        self.assertEqual("uri:443", client.config.server_url)
        self.assertEqual("client", client.config.client_id)
        self.assertEqual("secret", client.config.client_secret)
        self.assertEqual("project", client.config.project)
        self.assertEqual("branch", client.config.branch)

    @patch.dict(
        os.environ,
        {
            "TIGRIS_URI": "localhost:5000",
            "TIGRIS_PROJECT": "project_env",
        },
    )
    def test_init_with_partial_dict(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient({"project": "p1"})
        self.assertEqual("localhost:5000", client.config.server_url)
        self.assertEqual("p1", client.config.project)

    def test_init_with_config(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(
            conf=ClientConfig(
                server_url="test_url",
                project="test_project",
                client_id="test_client_id",
                client_secret="test_client_secret",
                branch="test_branch",
            )
        )
        self.assertEqual("test_url:443", client.config.server_url)
        self.assertEqual("test_client_id", client.config.client_id)
        self.assertEqual("test_client_secret", client.config.client_secret)
        self.assertEqual("test_project", client.config.project)
        self.assertEqual("test_branch", client.config.branch)

    def test_init_local_dev(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(
            {"server_url": "localhost:5000", "project": "test_project"}
        )
        self.assertEqual("localhost:5000", client.config.server_url)
        self.assertEqual("test_project", client.config.project)

    def test_init_failing_validation(self, ready_future):
        ready_future.return_value = self.done_future
        with self.assertRaisesRegex(
            ValueError, "`TIGRIS_PROJECT` environment variable"
        ):
            TigrisClient({"server_url": "localhost:5000"})

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
        self.assertEqual("project_env", client.config.project)
        self.assertEqual("branch_env", client.config.branch)

    def test_strip_https(self, ready_future):
        ready_future.return_value = self.done_future
        conf = ClientConfig(
            server_url="https://my.tigris.dev",
            project="p1",
            client_id="id",
            client_secret="secret",
        )
        client = TigrisClient(conf)
        self.assertEqual("my.tigris.dev:443", client.config.server_url)

        conf.server_url = "http://my.tigris.dev"
        client = TigrisClient(conf)
        self.assertEqual("my.tigris.dev:443", client.config.server_url)

    def test_get_db(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(ClientConfig(project="p1", server_url="localhost:5000"))
        self.assertEqual(client.config.branch, client.get_db().branch)
        self.assertEqual(client.config.project, client.get_db().project)

    def test_get_search(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(ClientConfig(project="p1", server_url="localhost:5000"))
        self.assertEqual(client.config.project, client.get_search().project)

    def test_get_vector_search(self, ready_future):
        ready_future.return_value = self.done_future
        client = TigrisClient(ClientConfig(project="p1", server_url="localhost:5000"))
        self.assertEqual("v1", client.get_vector_store("v1").name)
