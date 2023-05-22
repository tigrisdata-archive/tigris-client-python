from typing import Iterator, List

import grpc

from api.generated.server.v1.search_pb2 import (
    CreateDocumentRequest,
    CreateDocumentResponse,
    CreateOrReplaceDocumentRequest,
    CreateOrReplaceDocumentResponse,
    DeleteDocumentRequest,
    DeleteDocumentResponse,
    GetDocumentRequest,
    GetDocumentResponse,
    SearchIndexRequest,
    SearchIndexResponse,
    UpdateDocumentRequest,
    UpdateDocumentResponse,
)
from api.generated.server.v1.search_pb2_grpc import SearchStub
from tigrisdb.errors import TigrisServerError
from tigrisdb.types import ClientConfig, Document
from tigrisdb.types.search import DocStatus, IndexedDoc
from tigrisdb.types.search import Query as SearchQuery
from tigrisdb.types.search import Result as SearchResult
from tigrisdb.utils import marshal


class SearchIndex:
    __client: SearchStub
    __config: ClientConfig
    __name: str

    def __init__(self, index_name: str, client: SearchStub, config: ClientConfig):
        self.__client = client
        self.__name = index_name
        self.__config = config

    @property
    def project(self):
        return self.__config.project_name

    @property
    def name(self):
        return self.__name

    def search(self, query: SearchQuery, page: int = 1) -> SearchResult:
        req = SearchIndexRequest(project=self.project, index=self.name, page=page)
        query.__build__(req)
        try:
            result_iterator: Iterator[SearchIndexResponse] = self.__client.Search(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to search documents", e)
        # only single page of result will be returned
        for res in result_iterator:
            return SearchResult(_p=res)

    def create_many(self, docs: List[Document]) -> List[DocStatus]:
        doc_bytes = map(marshal, docs)
        req = CreateDocumentRequest(
            project=self.project, index=self.name, documents=doc_bytes
        )

        try:
            resp: CreateDocumentResponse = self.__client.Create(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to index documents", e)

        return [DocStatus(_p=d) for d in resp.status]

    def create_one(self, doc: Document) -> DocStatus:
        return self.create_many([doc])[0]

    def delete_many(self, doc_ids: List[str]) -> List[DocStatus]:
        req = DeleteDocumentRequest(project=self.project, index=self.name, ids=doc_ids)

        try:
            resp: DeleteDocumentResponse = self.__client.Delete(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to delete documents", e)

        return [DocStatus(_p=d) for d in resp.status]

    def delete_one(self, doc_id: str) -> DocStatus:
        return self.delete_many([doc_id])[0]

    def delete_by_query(self):
        raise NotImplementedError("deletion by filters is not supported yet")

    def create_or_replace_many(self, docs: List[Document]) -> List[DocStatus]:
        doc_bytes = map(marshal, docs)
        req = CreateOrReplaceDocumentRequest(
            project=self.project, index=self.name, documents=doc_bytes
        )
        try:
            resp: CreateOrReplaceDocumentResponse = self.__client.CreateOrReplace(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to create or replace documents", e)
        return [DocStatus(_p=d) for d in resp.status]

    def create_or_replace_one(self, doc: Document) -> DocStatus:
        return self.create_or_replace_many([doc])[0]

    def get_many(self, doc_ids: List[str]) -> List[IndexedDoc]:
        req = GetDocumentRequest(project=self.project, index=self.name, ids=doc_ids)

        try:
            resp: GetDocumentResponse = self.__client.Get(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to get documents", e)

        return [IndexedDoc(_p=hit) for hit in resp.documents]

    def get_one(self, doc_id: str) -> IndexedDoc:
        return self.get_many([doc_id])[0]

    def update_many(self, docs: List[Document]) -> List[DocStatus]:
        doc_bytes = map(marshal, docs)
        req = UpdateDocumentRequest(
            project=self.project, index=self.name, documents=doc_bytes
        )

        try:
            resp: UpdateDocumentResponse = self.__client.Update(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to update documents", e)

        return [*map(lambda d: DocStatus(_p=d), resp.status)]

    def update_one(self, doc: Document) -> DocStatus:
        return self.update_many([doc])[0]
