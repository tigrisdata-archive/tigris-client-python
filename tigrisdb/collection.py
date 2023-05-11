import grpc

from api.generated.server.v1.api_pb2 import InsertRequest, InsertResponse, ReadRequest
from api.generated.server.v1.api_pb2_grpc import TigrisStub
from tigrisdb.config import TigrisClientConfig
from tigrisdb.errors import TigrisException
from tigrisdb.types import Document
from tigrisdb.utils import bytes_to_doc, doc_to_bytes


class Collection:
    __client: TigrisStub
    __config: TigrisClientConfig
    __name: str

    def __init__(
        self, collection_name: str, client_stub: TigrisStub, config: TigrisClientConfig
    ):
        self.__client = client_stub
        self.__config = config
        self.__name = collection_name

    @property
    def project(self):
        return self.__config.project_name

    @property
    def branch(self):
        return self.__config.branch

    @property
    def name(self):
        return self.__name

    def insert_many(self, docs: list[Document]) -> bool:
        doc_bytes = map(doc_to_bytes, docs)
        req = InsertRequest(
            project=self.project,
            branch=self.branch,
            collection=self.name,
            documents=doc_bytes,
        )
        try:
            resp: InsertResponse = self.__client.Insert(req)
            if resp.status == "inserted":
                return True
            else:
                raise TigrisException(f"failed to insert docs: {resp.status}")
        except grpc.RpcError as e:
            raise TigrisException(f"failed to insert documents: {e}")

    def find_many(self) -> list[Document]:
        req = ReadRequest(
            project=self.project,
            branch=self.branch,
            collection=self.name,
            filter=doc_to_bytes({}),
        )
        try:
            doc_iterator = self.__client.Read(req)
        except grpc.RpcError as e:
            raise TigrisException(f"failed to read documents: {e}")

        docs: list[Document] = []
        for r in doc_iterator:
            docs.append(bytes_to_doc(r.data))

        return docs
