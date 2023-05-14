import grpc


class TigrisException(Exception):
    """
    Base class for all TigrisExceptions
    """

    msg: str

    def __init__(self, msg: str, **kwargs):
        self.msg = msg
        kwargs["message"] = msg
        super(TigrisException, self).__init__(kwargs)


# TODO: make this typesafe
class TigrisServerError(TigrisException):
    def __init__(self, msg: str, e: grpc.RpcError):
        super(TigrisServerError, self).__init__(msg, code=e.code(), details=e.details())
