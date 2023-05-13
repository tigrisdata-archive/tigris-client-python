from typing import Optional

import grpc


class StubRpcError(grpc.RpcError):
    def __init__(self, code: str, details: Optional[str]):
        self._code = code
        self._details = details

    def code(self):
        return self._code

    def details(self):
        return self._details
