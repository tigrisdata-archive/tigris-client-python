import abc

from tigrisdb.types import BaseOperator, Serializable


class Sort(Serializable, BaseOperator, abc.ABC):
    field = ""

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
