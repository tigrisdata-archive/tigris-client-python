from typing import Optional

import grpc


class StubRpcError(grpc.RpcError):
    def __init__(self, code: grpc.StatusCode, details: Optional[str]):
        self._code = code
        self._details = details

    def code(self):
        return self._code

    def details(self):
        return self._details


class UnavailableRpcError(StubRpcError):
    def __init__(self, details: Optional[str]):
        super().__init__(grpc.StatusCode.UNAVAILABLE, details)


class NotFoundRpcError(StubRpcError):
    def __init__(self, details: Optional[str]):
        super().__init__(grpc.StatusCode.NOT_FOUND, details)
