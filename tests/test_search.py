from unittest import TestCase
from unittest.mock import patch

from tigrisdb.search import Search
from tigrisdb.types import ClientConfig


@patch("api.generated.server.v1.search_pb2_grpc.SearchStub")
class SearchTest(TestCase):
    def setUp(self) -> None:
        self.client_config = ClientConfig(server_url="localhost:5000", project="db1")

    def test_get_index(self, grpc_search):
        mock_grpc = grpc_search()
        search = Search(mock_grpc, self.client_config)
        search_index = search.get_index("test-index")

        self.assertEqual("test-index", search_index.name)
        self.assertEqual(self.client_config.project, search_index.project)
