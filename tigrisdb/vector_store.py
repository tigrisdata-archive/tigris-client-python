from typing import List, Optional

import grpc

from tigrisdb.client import TigrisClient
from tigrisdb.errors import TigrisServerError
from tigrisdb.types import ClientConfig
from tigrisdb.types.filters import Filter
from tigrisdb.types.search import DocStatus, IndexedDoc, Query, Result, VectorField
from tigrisdb.types.vector import Document, DocWithScore


class VectorStore:
    def __init__(self, name: str, config: Optional[ClientConfig] = None):
        self.client = TigrisClient(config).get_search()
        self._index_name = name
        self.index = self.client.get_index(name)

    @property
    def name(self):
        return self._index_name

    def create_index(self, dimension: int):
        self.client.create_or_update_index(
            name=self.name,
            schema={
                "title": self.name,
                "additionalProperties": False,
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "text": {"type": "string"},
                    "metadata": {"type": "object"},
                    "embeddings": {
                        "type": "array",
                        "format": "vector",
                        "dimensions": dimension,
                    },
                },
            },
        )

    def add_documents(self, docs: List[Document]) -> List[DocStatus]:
        """Adds documents to index, if the index does not exist, create it. A `Document`
        is a dictionary with following structure:

        ```
        {
            "id": "optional id of a document",
            "text": "Actual content to store",
            "embeddings": "list of float values",
            "metadata": "optional metadata as dict"
        }
        ```

        - `id` is optional and automatically generated once documents are added to index
        - If `id` is given, any existing documents with matching `id` are replaced

        :param docs: list of documents to add to index
        :type docs: list[Document]
        :raises TigrisServerError: thrown i
        :return: List of `ids` for the added documents
        :rtype: list[DocStatus]
        """
        try:
            return self.index.create_many(docs)
        except TigrisServerError as e:
            if (
                e.code == grpc.StatusCode.NOT_FOUND
                and "search index not found" in e.details
            ):
                first_embedding = docs[0]["embeddings"] if docs else []
                inferred_dim = len(first_embedding) if first_embedding else 16
                self.create_index(inferred_dim)
                return self.index.create_many(docs)
            else:
                raise e

    def delete_documents(self, ids: List[str]) -> List[DocStatus]:
        """Delete documents from index.

        :param ids: list of document ids to delete
        :type ids: list[str]
        :return: `ids` of documents and deletion status for each
        :rtype: list[DocStatus]
        """
        return self.index.delete_many(ids)

    def get_documents(self, ids: List[str]) -> List[IndexedDoc]:
        """Retrieve documents from index. It will only have document `ids` found in the
        index.

        :param ids: list of document ids to retrieve
        :type ids: list[str]
        :return: list of documents and associated metadata
        :rtype: list[IndexedDoc]
        """
        return self.index.get_many(ids)

    def similarity_search(
        self, vector: List[float], k: int = 10, filter_by: Optional[Filter] = None
    ) -> List[DocWithScore]:
        """Perform a similarity search and returns documents most similar to the given
        vector with distance.

        :param vector: Search for documents closest to this vector
        :type vector: list[float]
        :param k: number of documents to return, defaults to 10
        :type k: int, optional
        :param filter_by: apply the filter to metadata to only return a subset of
                documents, defaults to None
        :type filter_by: Filter, optional
        :return: list of documents with similarity score (distance from given vector)
        :rtype: list[DocWithScore]
        """
        q = Query(
            vector_query=VectorField("embeddings", vector),
            filter_by=filter_by,
            hits_per_page=k,
        )
        r = self.search(q)
        return [DocWithScore(_h=hit) for hit in r.hits]

    def search(self, query: Query) -> Result:
        return self.index.search(query=query)
