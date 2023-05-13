import grpc

from api.generated.server.v1.api_pb2 import InsertRequest, InsertResponse, ReadRequest
from api.generated.server.v1.api_pb2_grpc import TigrisStub
from tigrisdb.errors import TigrisException, TigrisServerError
from tigrisdb.types import ClientConfig, Document
from tigrisdb.utils import bytes_to_dict, dict_to_bytes


class Collection:
    __client: TigrisStub
    __config: ClientConfig
    __name: str

    def __init__(
        self, collection_name: str, client_stub: TigrisStub, config: ClientConfig
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
        doc_bytes = map(dict_to_bytes, docs)
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
            raise TigrisServerError("failed to insert documents", e)

    def find_many(self) -> list[Document]:
        req = ReadRequest(
            project=self.project,
            branch=self.branch,
            collection=self.name,
            filter=dict_to_bytes({}),
        )
        try:
            doc_iterator = self.__client.Read(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to read documents", e)

        docs: list[Document] = []
        for r in doc_iterator:
            docs.append(bytes_to_dict(r.data))

        return docs
