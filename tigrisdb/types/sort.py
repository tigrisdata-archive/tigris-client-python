import abc

from tigrisdb.types import BaseOperator


class Sort(BaseOperator):
    field = ""

    @property
    @abc.abstractmethod
    def operator(self):
        raise NotImplementedError("Use either `Ascending` or `Descending`")

    def query(self):
        return {self.field: self.operator}


class Ascending(Sort):
    def __init__(self, field):
        self.field = field

    @property
    def operator(self):
        return "$asc"


class Descending(Sort):
    def __init__(self, field):
        self.field = field

    @property
    def operator(self):
        return "$desc"
