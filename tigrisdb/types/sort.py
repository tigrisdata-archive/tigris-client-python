import abc

from tigrisdb.types import Serializable


class Sort(Serializable):
    field = ""

    @property
    @abc.abstractmethod
    def operator(self):
        pass

    def as_obj(self):
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
