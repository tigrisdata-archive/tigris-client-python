import datetime
from unittest import TestCase
from unittest.mock import patch

from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp

from api.generated.server.v1.api_pb2 import Match, MatchField, SearchHit, SearchHitMeta
from api.generated.server.v1.observability_pb2 import Error as ProtoError
from api.generated.server.v1.search_pb2 import (
    CreateDocumentResponse,
    CreateOrReplaceDocumentResponse,
    DeleteDocumentRequest,
    DeleteDocumentResponse,
    DocStatus,
    GetDocumentResponse,
    SearchIndexRequest,
    SearchIndexResponse,
    UpdateDocumentResponse,
)
from tests import StubRpcError
from tigrisdb.errors import TigrisServerError
from tigrisdb.search_index import SearchIndex
from tigrisdb.types import ClientConfig, Document
from tigrisdb.types.search import Query as SearchQuery
from tigrisdb.utils import marshal, unmarshal


@patch("api.generated.server.v1.search_pb2_grpc.SearchStub")
class SearchIndexTest(TestCase):
    def setUp(self) -> None:
        self.client_config = ClientConfig(
            server_url="localhost:5000", project_name="db1"
        )
        self.index_name = "catalog"

    def test_search(self, grpc_search):
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Search.return_value = [
            SearchIndexResponse(hits=[SearchHit(data=marshal({"f": "v"}))])
        ]
        query = SearchQuery(q="hello world")
        resp = search_index.search(query, 3)
        self.assertEqual(1, len(resp.hits))
        self.assertEqual({"f": "v"}, resp.hits[0].doc)

        mock_grpc.Search.assert_called_once()
        called_with: SearchIndexRequest = mock_grpc.Search.call_args.args[0]
        self.assertEqual(called_with.project, search_index.project)
        self.assertEqual(called_with.index, search_index.name)
        self.assertEqual("hello world", called_with.q)
        self.assertEqual(3, called_with.page)

    def test_search_with_error(self, grpc_search):
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Search.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )
        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.search(SearchQuery())
        self.assertIsNotNone(e)

    def test_create_many(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Create.return_value = CreateDocumentResponse(
            status=[
                DocStatus(id="1"),
                DocStatus(id="2", error=ProtoError(message="conflict")),
            ]
        )

        resp = search_index.create_many(docs)
        self.assertEqual(resp[0].id, "1")
        self.assertIsNone(resp[0].error)
        self.assertEqual(resp[1].id, "2")
        self.assertRegex(resp[1].error.msg, "conflict")

        mock_grpc.Create.assert_called_once()
        called_with = mock_grpc.Create.call_args.args[0]
        self.assertEqual(called_with.project, search_index.project)
        self.assertEqual(called_with.index, search_index.name)
        self.assertEqual(list(map(unmarshal, called_with.documents)), docs)

    def test_create_many_with_error(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Create.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )

        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.create_many(docs)
        self.assertIsNotNone(e)

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

    def test_delete_many(self, grpc_search):
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Delete.return_value = DeleteDocumentResponse(
            status=[
                DocStatus(id="1"),
                DocStatus(id="2", error=ProtoError(message="conflict")),
            ]
        )
        resp = search_index.delete_many(["1", "2"])
        self.assertEqual(resp[0].id, "1")
        self.assertIsNone(resp[0].error)
        self.assertEqual(resp[1].id, "2")
        self.assertRegex(resp[1].error.msg, "conflict")

        mock_grpc.Delete.assert_called_once()
        called_with: DeleteDocumentRequest = mock_grpc.Delete.call_args.args[0]
        self.assertEqual(called_with.project, search_index.project)
        self.assertEqual(called_with.index, search_index.name)
        self.assertEqual(called_with.ids, ["1", "2"])

    def test_delete_many_with_error(self, grpc_search):
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Delete.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )

        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.delete_many(["id"])
        self.assertIsNotNone(e)

    def test_delete_one(self, grpc_search):
        with patch.object(
            SearchIndex, "delete_many", return_value="some_str"
        ) as mock_delete_many:
            search_index = SearchIndex(
                self.index_name, grpc_search(), self.client_config
            )
            search_index.delete_one("id")

        mock_delete_many.assert_called_once_with(["id"])

    def test_create_or_replace_many(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.CreateOrReplace.return_value = CreateOrReplaceDocumentResponse(
            status=[
                DocStatus(id="1"),
                DocStatus(id="2", error=ProtoError(message="conflict")),
            ]
        )

        resp = search_index.create_or_replace_many(docs)
        self.assertEqual(resp[0].id, "1")
        self.assertIsNone(resp[0].error)
        self.assertEqual(resp[1].id, "2")
        self.assertRegex(resp[1].error.msg, "conflict")

        mock_grpc.CreateOrReplace.assert_called_once()
        called_with = mock_grpc.CreateOrReplace.call_args.args[0]
        self.assertEqual(called_with.project, search_index.project)
        self.assertEqual(called_with.index, search_index.name)
        self.assertEqual(list(map(unmarshal, called_with.documents)), docs)

    def test_create_or_replace_many_with_error(self, grpc_search):
        docs = [{"id": 1, "name": "shoe"}, {"id": 2, "name": "jacket"}]
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.CreateOrReplace.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )

        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.create_or_replace_many(docs)
        self.assertIsNotNone(e)

    def test_create_or_replace_one(self, grpc_search):
        doc: Document = {"item_id": 1, "name": "shoe", "brand": "adidas"}
        with patch.object(
            SearchIndex, "create_or_replace_many", return_value="some_str"
        ) as mock_replace_any:
            search_index = SearchIndex(
                self.index_name, grpc_search(), self.client_config
            )
            search_index.create_or_replace_one(doc)

        mock_replace_any.assert_called_once_with([doc])

    def test_get_many(self, grpc_search):
        docs = [
            {"id": "1", "title": "नमस्ते to India", "tags": ["travel"]},
            {"id": "2", "title": "reliable systems 🙏", "tags": ["it"]},
        ]
        ts, proto_ts = (
            datetime.datetime.fromisoformat("2023-05-05T10:00:00+00:00"),
            ProtoTimestamp(),
        )
        proto_ts.FromDatetime(ts)
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        expected_resp = GetDocumentResponse()
        expected_resp.documents.extend(
            [
                SearchHit(
                    data=marshal(docs[0]),
                    metadata=SearchHitMeta(
                        created_at=proto_ts,
                        updated_at=proto_ts,
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
        self.assertEqual(len(docs), len(resp))
        self.assertEqual(docs[0], resp[0].doc)
        self.assertEqual(ts, resp[0].meta.created_at)
        self.assertEqual(ts, resp[0].meta.updated_at)
        self.assertEqual("25.0", resp[0].meta.text_match.score)
        self.assertEqual(["f1"], resp[0].meta.text_match.fields)
        self.assertEqual(34.35, resp[0].meta.text_match.vector_distance)
        self.assertEqual(docs[1], resp[1].doc)

    def test_get_many_with_error(self, grpc_search):
        search_index = SearchIndex(self.index_name, grpc_search(), self.client_config)
        mock_grpc = grpc_search()
        mock_grpc.Get.side_effect = StubRpcError(
            code="Unavailable", details="operational failure"
        )

        with self.assertRaisesRegex(TigrisServerError, "operational failure") as e:
            search_index.get_many(["id"])
        self.assertIsNotNone(e)

    def test_get_one(self, grpc_search):
        with patch.object(
            SearchIndex, "get_many", return_value="some_str"
        ) as mock_get_many:
            search_index = SearchIndex(
                self.index_name, grpc_search(), self.client_config
            )
            search_index.get_one("id")

        mock_get_many.assert_called_once_with(["id"])

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
