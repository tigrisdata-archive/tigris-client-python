from dataclasses import InitVar, dataclass, field
from datetime import datetime
from typing import List, Optional, Union

from api.generated.server.v1.api_pb2 import Match as ProtoMatch
from api.generated.server.v1.api_pb2 import SearchHit as ProtoSearchHit
from api.generated.server.v1.api_pb2 import SearchHitMeta as ProtoSearchHitMeta
from api.generated.server.v1.search_pb2 import DocStatus as ProtoDocStatus
from api.generated.server.v1.search_pb2 import (
    SearchIndexRequest as ProtoSearchIndexRequest,
)
from api.generated.server.v1.search_pb2 import (
    SearchIndexResponse as ProtoSearchIndexResponse,
)
from tigrisdb.errors import TigrisException
from tigrisdb.types import Document, Serializable
from tigrisdb.types.sort import Sort
from tigrisdb.utils import marshal, unmarshal

dataclass_default_proto_field = field(
    default=None, repr=False, compare=False, hash=False
)


@dataclass()
class FacetSize(Serializable):
    field: str
    size: int = 10

    def as_obj(self):
        return {"size": self.size, "type": "value"}


FacetField = Union[str, FacetSize]


@dataclass()
class VectorField(Serializable):
    field: str
    vector: List[float]

    def as_obj(self):
        return {self.field: self.vector}


# TODO: add filter, collation
@dataclass()
class Query:
    q: str = ""
    search_fields: List[str] = field(default_factory=list)
    vector_query: VectorField = None
    facet_by: Union[str, List[FacetField]] = field(default_factory=list)
    sort_by: Union[Sort, List[Sort]] = field(default_factory=list)
    group_by: Union[str, List[str]] = field(default_factory=list)
    include_fields: List[str] = field(default_factory=list)
    exclude_fields: List[str] = field(default_factory=list)
    hits_per_page: int = 20

    def __build__(self, req: ProtoSearchIndexRequest):
        req.q = self.q or ""
        if self.search_fields:
            req.search_fields.extend(self.search_fields)
        if self.vector_query:
            req.vector = marshal(self.vector_query.as_obj())
        if self.facet_by:
            f = {}
            if isinstance(self.facet_by, str):
                f[self.facet_by] = FacetSize(self.facet_by).as_obj()
            elif isinstance(self.facet_by, list):
                for facet in self.facet_by:
                    if isinstance(facet, str):
                        f[facet] = FacetSize(facet).as_obj()
                    elif isinstance(facet, FacetSize):
                        f[facet.field] = facet.as_obj()
            req.facet = marshal(f)
        if self.sort_by:
            order = []
            if isinstance(self.sort_by, Sort):
                order.append(self.sort_by.as_obj())
            elif isinstance(self.sort_by, list):
                order = [s.as_obj() for s in self.sort_by]
            req.sort = marshal(order)
        if self.group_by:
            g = [self.group_by] if isinstance(self.group_by, str) else self.group_by
            req.group_by = marshal(g)
        if self.include_fields:
            req.include_fields.extend(self.include_fields)
        if self.exclude_fields:
            req.exclude_fields.extend(self.exclude_fields)
        req.page_size = self.hits_per_page


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
            self.doc = unmarshal(_p.data)
            self.meta = DocMeta(_p=_p.metadata)


@dataclass
class Result:
    hits: List[IndexedDoc] = field(default_factory=list)
    _p: InitVar[ProtoSearchIndexResponse] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchIndexResponse):
        if _p:
            self.hits = [IndexedDoc(_p=h) for h in _p.hits]
