import os
from typing import Optional

import grpc

from api.generated.server.v1 import api_pb2_grpc as tigris_grpc
from tigrisdb.auth import AuthGateway
from tigrisdb.database import Database
from tigrisdb.errors import TigrisException
from tigrisdb.types import ClientConfig


class TigrisClient(object):
    __LOCAL_SERVER = "localhost:8081"

    __tigris_stub: tigris_grpc.TigrisStub
    __config: ClientConfig

    def __init__(self, config: Optional[ClientConfig]):
        os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

        if not config:
            config = ClientConfig()
        self.__config = config
        if not config.server_url:
            config.server_url = TigrisClient.__LOCAL_SERVER
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
            channel = grpc.insecure_channel(config.server_url)
        else:
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

        self.__tigris_stub = tigris_grpc.TigrisStub(channel)

    def get_db(self):
        return Database(self.__tigris_stub, self.__config)
