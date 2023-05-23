import abc
from typing import Any, Dict, Union

from tigrisdb.types import BaseOperator, Serializable

from .selector import SelectorFilter


class LogicalFilter(Serializable, BaseOperator, abc.ABC):
    def __init__(self, *args: Union[SelectorFilter, Any]):
        self.filters = args

    def query(self) -> Dict:
        if not self.filters:
            return {}
        if len(self.filters) == 1:
            return self.filters[0].query()
        gen = [f.query() for f in self.filters]
        return {self.operator: gen}


class And(LogicalFilter):
    @property
    def operator(self):
        return "$and"


class Or(LogicalFilter):
    @property
    def operator(self):
        return "$or"
