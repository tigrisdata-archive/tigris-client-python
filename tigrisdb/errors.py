from typing import cast

import grpc


class TigrisException(Exception):
    """Base class for all TigrisExceptions."""

    msg: str

    def __init__(self, msg: str, **kwargs):
        self.msg = msg
        kwargs["message"] = msg
        super(TigrisException, self).__init__(kwargs)


# TODO: make this typesafe
class TigrisServerError(TigrisException):
    def __init__(self, msg: str, e: grpc.RpcError):
        if isinstance(e.code(), grpc.StatusCode):
            self.code = cast(grpc.StatusCode, e.code())
        else:
            self.code = grpc.StatusCode.UNKNOWN

        self.details = e.details()
        super(TigrisServerError, self).__init__(
            msg, code=self.code.name, details=self.details
        )
        self.__suppress_context__ = True
