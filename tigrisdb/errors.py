class TigrisException(Exception):
    """
    Base class for all TigrisExceptions
    """

    msg: str

    def __init__(self, msg: str):
        self.msg = msg
        super(TigrisException, self).__init__(self.msg)
