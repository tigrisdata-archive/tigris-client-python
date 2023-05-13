import time
from unittest import TestCase
from unittest.mock import MagicMock, patch

import grpc

from api.generated.server.v1.auth_pb2 import GetAccessTokenResponse
from tests import StubRpcError
from tigrisdb.auth import AuthGateway
from tigrisdb.errors import TigrisServerError
from tigrisdb.types import ClientConfig
from tigrisdb.utils import dict_to_b64


@patch("api.generated.server.v1.auth_pb2_grpc.AuthStub")
@patch("grpc.channel_ready_future")
class AuthGatewayTest(TestCase):
    def setUp(self) -> None:
        self.done_future = MagicMock(grpc.Future)
        self.client_config = ClientConfig(
            server_url="localhost:5000", project_name="db1"
        )

    def test_get_access_token_with_valid_token_refresh_window(
        self, channel_ready_future, grpc_auth
    ):
        channel_ready_future.return_value = self.done_future
        expiration_time = time.time()
        mock_grpc_auth, expected_token = grpc_auth(), _encoded_token(expiration_time)
        mock_grpc_auth.GetAccessToken.return_value = GetAccessTokenResponse(
            access_token=expected_token
        )

        auth_gateway = AuthGateway(self.client_config)
        actual_token = auth_gateway.get_access_token()
        self.assertEqual(expected_token, actual_token)
        next_refresh = auth_gateway.__getattribute__("_AuthGateway__next_refresh_time")
        # refresh time is within 11 minutes of expiration time
        self.assertLessEqual(expiration_time - next_refresh, 660)

    def test_get_access_token_with_rpc_failure(self, channel_ready_future, grpc_auth):
        channel_ready_future.return_value = self.done_future
        mock_grpc_auth = grpc_auth()
        mock_grpc_auth.GetAccessToken.side_effect = StubRpcError(
            code="Unavailable", details=""
        )

        auth_gateway = AuthGateway(self.client_config)
        with self.assertRaisesRegex(
            TigrisServerError, "failed to get access token"
        ) as e:
            auth_gateway.get_access_token()
        self.assertIsNotNone(e)

    def test_should_refresh_with_expired_token(self, channel_ready_future, grpc_auth):
        channel_ready_future.return_value = self.done_future
        auth_gateway = AuthGateway(self.client_config)

        self.assertTrue(auth_gateway.should_refresh())
        auth_gateway.__setattr__("_AuthGateway__cached_token", "xyz")
        auth_gateway.__setattr__("_AuthGateway__next_refresh_time", time.time() + 5)
        self.assertFalse(auth_gateway.should_refresh())
        auth_gateway.__setattr__("_AuthGateway__next_refresh_time", time.time() - 5)
        self.assertTrue(auth_gateway.should_refresh())

    def test_should_refresh_without_cached_token(self, channel_ready_future, grpc_auth):
        channel_ready_future.return_value = self.done_future
        auth_gateway = AuthGateway(self.client_config)

        self.assertTrue(auth_gateway.should_refresh())
        auth_gateway.__setattr__("_AuthGateway__cached_token", "xyz")
        self.assertTrue(auth_gateway.should_refresh())
        auth_gateway.__setattr__("_AuthGateway__next_refresh_time", time.time() + 10)
        self.assertFalse(auth_gateway.should_refresh())

    def test_get_auth_headers(self, channel_ready_future, grpc_auth):
        channel_ready_future.return_value = self.done_future
        auth_gateway = AuthGateway(self.client_config)

        auth_gateway.__setattr__("_AuthGateway__cached_token", "xyz")
        auth_gateway.__setattr__("_AuthGateway__next_refresh_time", time.time() + 10)
        self.assertFalse(auth_gateway.should_refresh())
        expected_headers = [
            ("authorization", "Bearer xyz"),
            ("user-agent", "tigris-client-python.grpc"),
            ("destination-name", self.client_config.server_url),
        ]
        self.assertCountEqual(expected_headers, auth_gateway.get_auth_headers(None))


def _encoded_token(expiration: float):
    return f'token.{dict_to_b64({"exp": expiration})}'
