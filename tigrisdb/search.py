import grpc

from api.generated.server.v1.search_pb2 import (
    CreateOrUpdateIndexRequest,
    CreateOrUpdateIndexResponse,
    DeleteIndexRequest,
    DeleteIndexResponse,
)
from api.generated.server.v1.search_pb2_grpc import SearchStub
from tigrisdb.errors import TigrisException, TigrisServerError
from tigrisdb.search_index import SearchIndex
from tigrisdb.types import ClientConfig
from tigrisdb.utils import schema_to_bytes


class Search:
    __client: SearchStub
    __config: ClientConfig

    def __init__(self, client: SearchStub, config: ClientConfig):
        self.__client = client
        self.__config = config

    @property
    def project(self):
        return self.__config.project_name

    def create_or_update_index(self, name: str, schema: dict) -> SearchIndex:
        req = CreateOrUpdateIndexRequest(
            project=self.project, name=name, schema=schema_to_bytes(schema)
        )
        try:
            resp: CreateOrUpdateIndexResponse = self.__client.CreateOrUpdateIndex(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to create search index", e)

        if resp.status == "created":
            return SearchIndex(
                index_name=name, client=self.__client, config=self.__config
            )

        raise TigrisException(f"Invalid response to create search index: {resp.status}")

    def delete_index(self, name: str) -> bool:
        req = DeleteIndexRequest(name=name, project=self.project)
        try:
            resp: DeleteIndexResponse = self.__client.DeleteIndex(req)
        except grpc.RpcError as e:
            raise TigrisServerError("failed to delete search index", e)

        return resp.status == "deleted"

    def get_index(self, name: str) -> SearchIndex:
        return SearchIndex(index_name=name, client=self.__client, config=self.__config)
