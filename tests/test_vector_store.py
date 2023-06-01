from unittest import TestCase
from unittest.mock import MagicMock, Mock, call, patch

from tests import NotFoundRpcError
from tigrisdb.errors import TigrisServerError
from tigrisdb.search import Search
from tigrisdb.search_index import SearchIndex
from tigrisdb.types.search import (
    DocMeta,
    DocStatus,
    IndexedDoc,
    Query,
    Result,
    TextMatchInfo,
    VectorField,
)
from tigrisdb.types.vector import Document
from tigrisdb.vector_store import VectorStore

doc: Document = {
    "text": "Hello world vector embed",
    "embeddings": [1.2, 2.3, 4.5],
    "metadata": {"category": "shoes"},
}


class VectorStoreTest(TestCase):
    def setUp(self) -> None:
        self.mock_index = Mock(spec=SearchIndex)
        self.mock_client = Mock(spec=Search)
        with patch("tigrisdb.client.TigrisClient.__new__") as mock_tigris:
            instance = MagicMock()
            mock_tigris.return_value = instance
            instance.get_search.return_value = self.mock_client
            self.mock_client.get_index.return_value = self.mock_index
            self.store = VectorStore("my_vectors")

    def test_add_documents_when_index_not_found(self):
        # throw error on first call and succeed on second
        self.mock_index.create_many.side_effect = [
            TigrisServerError("", NotFoundRpcError("search index not found")),
            [DocStatus(id="1")],
        ]

        resp = self.store.add_documents([doc])
        self.assertEqual([DocStatus(id="1")], resp)
        self.assertEqual(self.mock_index.create_many.call_count, 2)
        self.mock_index.create_many.assert_has_calls([call([doc]), call([doc])])

        # create_or_update_index gets called once
        expected_schema = {
            "title": self.store.name,
            "additionalProperties": False,
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "text": {"type": "string"},
                "metadata": {"type": "object"},
                "embeddings": {"type": "array", "format": "vector", "dimensions": 3},
            },
        }

        self.mock_client.create_or_update_index.assert_called_once_with(
            name=self.store.name, schema=expected_schema
        )

    def test_add_documents_when_index_exists(self):
        self.mock_index.create_many.return_value = [DocStatus(id="1")]
        resp = self.store.add_documents([doc])
        self.assertEqual([DocStatus(id="1")], resp)

        # no calls to create_or_update_index
        self.mock_client.assert_not_called()

    def test_add_documents_when_project_not_found(self):
        self.mock_index.create_many.side_effect = [
            TigrisServerError("", NotFoundRpcError("project not found")),
            [DocStatus(id="1")],
        ]
        with self.assertRaisesRegex(TigrisServerError, "project not found"):
            self.store.add_documents([doc])
        self.mock_index.create_many.assert_called_once_with([doc])

    def test_delete_documents(self):
        self.store.delete_documents(["id"])
        self.mock_index.delete_many.assert_called_once_with(["id"])

    def test_get_documents(self):
        self.store.get_documents(["id"])
        self.mock_index.get_many.assert_called_once_with(["id"])

    def test_similarity_search(self):
        self.mock_index.search.return_value = Result(
            hits=[
                IndexedDoc(
                    doc=doc,
                    meta=DocMeta(text_match=TextMatchInfo(vector_distance=0.1234)),
                )
            ]
        )
        resp = self.store.similarity_search([1, 1, 1], 12)
        self.assertEqual(1, len(resp))
        self.assertEqual(doc, resp[0].doc)
        self.assertEqual(0.1234, resp[0].score)

        self.mock_index.search.assert_called_once_with(
            query=Query(
                vector_query=VectorField(field="embeddings", vector=[1, 1, 1]),
                hits_per_page=12,
            )
        )
