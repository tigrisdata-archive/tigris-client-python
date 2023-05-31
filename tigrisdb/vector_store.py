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

    def _ensure_index(self, dimension: int):
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
        # try inserting, if index is not found, ensure index and insert again
        try:
            return self.index.create_many(docs)
        except TigrisServerError as e:
            if (
                e.code == grpc.StatusCode.NOT_FOUND
                and "search index not found" in e.details
            ):
                first_embedding = docs[0]["embeddings"] if docs else []
                inferred_dim = len(first_embedding) if first_embedding else 16
                self._ensure_index(inferred_dim)
                return self.index.create_many(docs)
            else:
                raise e

    def delete_documents(self, ids: List[str]) -> List[DocStatus]:
        return self.index.delete_many(ids)

    def get_documents(self, ids: List[str]) -> List[IndexedDoc]:
        return self.index.get_many(ids)

    def similarity_search(
        self, vector: List[float], k: int = 10, filter_by: Optional[Filter] = None
    ) -> List[DocWithScore]:
        q = Query(
            vector_query=VectorField("embeddings", vector),
            filter_by=filter_by,
            hits_per_page=k,
        )
        r = self.search(q)
        return [DocWithScore(_h=hit) for hit in r.hits]

    def search(self, query: Query) -> Result:
        return self.index.search(query=query)
