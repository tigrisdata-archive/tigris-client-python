from random import randint
from time import time

import grpc

from api.generated.server.v1 import auth_pb2_grpc as tigris_auth
from api.generated.server.v1.auth_pb2 import (
    CLIENT_CREDENTIALS,
    GetAccessTokenRequest,
    GetAccessTokenResponse,
)
from tigrisdb.errors import TigrisException, TigrisServerError
from tigrisdb.types import ClientConfig
from tigrisdb.utils import b64_to_object


class AuthGateway(grpc.AuthMetadataPlugin):
    __cached_token: str = ""
    __next_refresh_time: float = 0.0
    __config: ClientConfig
    __auth_stub: tigris_auth.AuthStub

    def __init__(self, config: ClientConfig):
        super(grpc.AuthMetadataPlugin, self).__init__()
        self.__config = config
        channel = grpc.secure_channel(config.server_url, grpc.ssl_channel_credentials())
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            raise TigrisException(f"Auth connection timed out: {config.server_url}")
        self.__auth_stub = tigris_auth.AuthStub(channel)

    def get_access_token(self):
        if self.should_refresh():
            req = GetAccessTokenRequest(
                grant_type=CLIENT_CREDENTIALS,
                client_id=self.__config.client_id,
                client_secret=self.__config.client_secret,
            )
            try:
                resp: GetAccessTokenResponse = self.__auth_stub.GetAccessToken(req)
                self.__cached_token = resp.access_token
                token_meta = b64_to_object(self.__cached_token.split(".")[1] + "==")
                exp = float(token_meta["exp"])
                self.__next_refresh_time = exp - 300 - float(randint(0, 300) + 60)
            except grpc.RpcError as e:
                raise TigrisServerError("failed to get access token", e)
        return self.__cached_token

    def should_refresh(self):
        return (not self.__cached_token) or time() >= self.__next_refresh_time

    def get_auth_headers(self, context: grpc.AuthMetadataContext):
        headers = (
            ("authorization", f"Bearer {self.get_access_token()}"),
            ("user-agent", "tigris-client-python.grpc"),
            ("destination-name", self.__config.server_url),
        )
        return headers

    def __call__(self, context, callback):
        """Implements authentication by passing metadata to a callback.

        This method will be invoked asynchronously in a separate thread.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        """
        callback(self.get_auth_headers(context), None)
