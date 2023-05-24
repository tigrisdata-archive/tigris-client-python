from typing import Union

from .logical import And, LogicalFilter, Or  # noqa: F401
from .selector import (  # noqa: F401
    GT,
    GTE,
    LT,
    LTE,
    Contains,
    Eq,
    Not,
    Regex,
    SelectorFilter,
)

Filter = Union[LogicalFilter, SelectorFilter]
