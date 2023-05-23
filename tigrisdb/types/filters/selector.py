import abc
from typing import Any, Dict

from tigrisdb.types import BaseOperator, Serializable


class SelectorFilter(Serializable, BaseOperator, abc.ABC):
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value

    def query(self) -> Dict:
        return {self.field: {self.operator: self.value}}


class Eq(SelectorFilter):
    @property
    def operator(self):
        return ""

    def query(self) -> Dict:
        return {self.field: self.value}


class Not(SelectorFilter):
    @property
    def operator(self):
        return "$not"


class GT(SelectorFilter):
    @property
    def operator(self):
        return "$gt"


class GTE(SelectorFilter):
    @property
    def operator(self):
        return "$gte"


class LT(SelectorFilter):
    @property
    def operator(self):
        return "$lt"


class LTE(SelectorFilter):
    @property
    def operator(self):
        return "$lte"


class Regex(SelectorFilter):
    @property
    def operator(self):
        return "$regex"


class Contains(SelectorFilter):
    @property
    def operator(self):
        return "$contains"
