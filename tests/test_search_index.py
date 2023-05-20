from unittest import TestCase
from unittest.mock import patch

from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp

from api.generated.server.v1.api_pb2 import Match, MatchField, SearchHit, SearchHitMeta
from api.generated.server.v1.observability_pb2 import Error as ProtoError
from api.generated.server.v1.search_pb2 import (
    DocStatus,
    GetDocumentResponse,
    UpdateDocumentResponse,
)
from tests import StubRpcError
from tigrisdb.errors import TigrisServerError
from tigrisdb.search_index import SearchIndex
from tigrisdb.types import ClientConfig, Document
from tigrisdb.utils import marshal, unmarshal


@patch("api.generated.server.v1.search_pb2_grpc.SearchStub")
class SearchIndexTest(TestCase):
    def setUp(self) -> None:
        self.client_config = ClientConfig(
            server_url="localhost:5000", project_name="db1"
        )
        self.index_name = "catalog"

    def test_create_one(self, grpc_search):
        doc: Document = {"item_id": 1, "name": "shoe", "brand": "adidas"}
        with patch.object(
            SearchIndex, "create_many", return_value="some_str"
        ) as mock_create_many:
            search_index = SearchIndex(
                self.index_name, grpc_search(), self.client_config
            )
            search_index.create_one(doc)

        mock_create_many.assert_called_once_with([doc])

    def test_get_many(self, grpc_search):
        docs = [
            {"id": "1", "title": "नमस्ते to India", "tags": ["travel"]},
            {"id": "2", "title": "reliable systems 🙏", "tags": ["it"]},
        ]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        ts = ProtoTimestamp()
        expected_resp = GetDocumentResponse()
        expected_resp.documents.extend(
            [
                SearchHit(
                    data=marshal(docs[0]),
                    metadata=SearchHitMeta(
                        created_at=ts.FromJsonString("2023-05-05T10:00:00Z"),
                        # updated_at=Timestamp().FromJsonString("2022-11-07T04:30:00Z"),
                        match=Match(
                            fields=[MatchField(name="f1")],
                            score="25.0",
                            vector_distance=34.35,
                        ),
                    ),
                ),
                SearchHit(data=marshal(docs[1])),
            ]
        )
        mock_grpc.Get.return_value = expected_resp
        resp = search_index.get_many(list(map(lambda d: d["id"], docs)))
        print(resp)

    def test_update_many(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Update.return_value = UpdateDocumentResponse(
            status=[
                DocStatus(id="1"),
                DocStatus(id="2", error=ProtoError(message="conflict")),
            ]
        )

        resp = search_index.update_many(docs)
        self.assertEqual(resp[0].id, "1")
        self.assertIsNone(resp[0].error)
        self.assertEqual(resp[1].id, "2")
        self.assertRegex(resp[1].error.msg, "conflict")

        mock_grpc.Update.assert_called_once()
        called_with = mock_grpc.Update.call_args.args[0]
        self.assertEqual(called_with.project, search_index.project)
        self.assertEqual(called_with.index, search_index.name)
        self.assertEqual(list(map(unmarshal, called_with.documents)), docs)

    def test_update_many_with_error(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Update.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )

        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.update_many(docs)
        self.assertIsNotNone(e)

    def test_update_one(self, grpc_search):
        doc: Document = {"item_id": 1, "name": "shoe", "brand": "adidas"}
        with patch.object(
            SearchIndex, "update_many", return_value="some_str"
        ) as mock_update_many:
            search_index = SearchIndex(
                self.index_name, grpc_search(), self.client_config
            )
            search_index.update_one(doc)

        mock_update_many.assert_called_once_with([doc])
