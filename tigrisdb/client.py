import os
from typing import Union

import grpc

from api.generated.server.v1.api_pb2_grpc import TigrisStub
from api.generated.server.v1.search_pb2_grpc import SearchStub
from tigrisdb.auth import AuthGateway
from tigrisdb.database import Database
from tigrisdb.errors import TigrisException
from tigrisdb.search import Search
from tigrisdb.types import ClientConfig
from tigrisdb.vector_store import VectorStore


class TigrisClient(object):
    __PREVIEW_URI = "api.preview.tigrisdata.cloud"

    __tigris_client: TigrisStub
    __search_client: SearchStub
    __config: ClientConfig

    def __init__(self, conf: Union[ClientConfig, dict, None] = None):
        os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

        if not conf:
            config = ClientConfig()
        elif isinstance(conf, dict):
            config = ClientConfig()
            config.project_name = conf.get("project", config.project_name)
            config.server_url = conf.get("server_url", config.server_url)
            config.client_id = conf.get("client_id", config.client_id)
            config.client_secret = conf.get("client_secret", config.client_secret)
            config.branch = conf.get("branch", config.branch)
        else:
            config = conf

        self.__config = config
        if config.server_url.startswith("https://"):
            config.server_url = config.server_url.replace("https://", "")
        if config.server_url.startswith("http://"):
            config.server_url = config.server_url.replace("http://", "")
        if ":" not in config.server_url:
            config.server_url = f"{config.server_url}:443"

        is_local_dev = any(
            map(
                lambda k: k in config.server_url,
                ["localhost", "127.0.0.1", "tigrisdb-local-server:", "[::1]"],
            )
        )

        if is_local_dev:
            config.validate()
            channel = grpc.insecure_channel(config.server_url)
        else:
            config.validate(with_creds=True)
            auth_gtwy = AuthGateway(config)
            channel_creds = grpc.ssl_channel_credentials()
            call_creds = grpc.metadata_call_credentials(auth_gtwy, name="auth gateway")
            channel = grpc.secure_channel(
                config.server_url,
                grpc.composite_channel_credentials(channel_creds, call_creds),
            )

        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            raise TigrisException(f"Connection timed out {config.server_url}")

        self.__tigris_client = TigrisStub(channel)
        self._database = Database(self.__tigris_client, self.__config)
        self.__search_client = SearchStub(channel)
        self._search = Search(self.__search_client, self.__config)

    @property
    def config(self):
        return self.__config

    def get_db(self) -> Database:
        return self._database

    def get_search(self) -> Search:
        return self._search

    def get_vector_store(self, name: str) -> VectorStore:
        return VectorStore(self._search, name)
