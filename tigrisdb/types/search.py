from dataclasses import InitVar, dataclass, field
from datetime import datetime
from typing import List, Optional

from api.generated.server.v1.api_pb2 import Match as ProtoMatch
from api.generated.server.v1.api_pb2 import SearchHit as ProtoSearchHit
from api.generated.server.v1.api_pb2 import SearchHitMeta as ProtoSearchHitMeta
from api.generated.server.v1.search_pb2 import DocStatus as ProtoDocStatus
from api.generated.server.v1.search_pb2 import (
    SearchIndexResponse as ProtoSearchIndexResponse,
)
from tigrisdb.errors import TigrisException
from tigrisdb.types import Document
from tigrisdb.utils import bytes_to_dict


class Query:
    q: str


dataclass_default_proto_field = field(
    default=None, repr=False, compare=False, hash=False
)


@dataclass
class DocStatus:
    id: str = None
    error: Optional[TigrisException] = None
    _p: InitVar[ProtoDocStatus] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoDocStatus):
        if _p:
            self.error = (
                TigrisException(_p.error.message) if _p.HasField("error") else None
            )
            self.id = _p.id


@dataclass
class TextMatchInfo:
    score: str = None
    vector_distance: Optional[float] = None
    fields: List[str] = field(default_factory=list)
    _p: InitVar[ProtoMatch] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoMatch):
        if _p:
            # todo: look to remove this has field
            self.fields = [f.name for f in _p.fields]
            self.vector_distance = _p.vector_distance
            self.score = _p.score


@dataclass
class DocMeta:
    created_at: datetime = None
    updated_at: datetime = None
    text_match: TextMatchInfo = None
    _p: InitVar[ProtoSearchHitMeta] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchHitMeta):
        if _p:
            # todo: add conversion tests
            self.created_at = _p.created_at.ToDatetime()
            self.updated_at = _p.updated_at.ToDatetime()
            self.text_match = TextMatchInfo(_p=_p.match)


@dataclass
class IndexedDoc:
    doc: Document = None
    meta: DocMeta = None
    _p: InitVar[ProtoSearchHit] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchHit):
        if _p:
            self.doc = bytes_to_dict(_p.data)
            self.meta = DocMeta(_p=_p.metadata)


@dataclass
class Result:
    hits: List[IndexedDoc] = field(default_factory=list)
    _p: InitVar[ProtoSearchIndexResponse] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchIndexResponse):
        if _p:
            self.hits = [IndexedDoc(_p=h) for h in _p.hits]
