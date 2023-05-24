from dataclasses import InitVar, dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional, Union

from api.generated.server.v1.api_pb2 import FacetCount as ProtoFacetCount
from api.generated.server.v1.api_pb2 import FacetStats as ProtoFacetStats
from api.generated.server.v1.api_pb2 import GroupedSearchHits as ProtoGroupedHits
from api.generated.server.v1.api_pb2 import Match as ProtoMatch
from api.generated.server.v1.api_pb2 import Page as ProtoPage
from api.generated.server.v1.api_pb2 import SearchFacet as ProtoSearchFacet
from api.generated.server.v1.api_pb2 import SearchHit as ProtoSearchHit
from api.generated.server.v1.api_pb2 import SearchHitMeta as ProtoSearchHitMeta
from api.generated.server.v1.api_pb2 import SearchMetadata as ProtoSearchMeta
from api.generated.server.v1.search_pb2 import DocStatus as ProtoDocStatus
from api.generated.server.v1.search_pb2 import (
    SearchIndexRequest as ProtoSearchIndexRequest,
)
from api.generated.server.v1.search_pb2 import (
    SearchIndexResponse as ProtoSearchIndexResponse,
)
from tigrisdb.errors import TigrisException
from tigrisdb.types import Document, Serializable
from tigrisdb.types.filters import Filter
from tigrisdb.types.sort import Sort
from tigrisdb.utils import marshal, unmarshal

dataclass_default_proto_field = field(
    default=None, repr=False, compare=False, hash=False
)


@dataclass
class FacetSize(Serializable):
    field: str
    size: int = 10

    def query(self):
        return {"size": self.size, "type": "value"}


FacetField = Union[str, FacetSize]


@dataclass
class VectorField(Serializable):
    field: str
    vector: List[float]

    def query(self):
        return {self.field: self.vector}


# TODO: add filter, collation
@dataclass
class Query:
    q: str = ""
    search_fields: List[str] = field(default_factory=list)
    vector_query: VectorField = None
    filter_by: Optional[Filter] = None
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
            req.vector = marshal(self.vector_query.query())
        if self.filter_by:
            req.filter = marshal(self.filter_by.query())
        if self.facet_by:
            f = {}
            if isinstance(self.facet_by, str):
                f[self.facet_by] = FacetSize(self.facet_by).query()
            elif isinstance(self.facet_by, list):
                for facet in self.facet_by:
                    if isinstance(facet, str):
                        f[facet] = FacetSize(facet).query()
                    elif isinstance(facet, FacetSize):
                        f[facet.field] = facet.query()
            req.facet = marshal(f)
        if self.sort_by:
            order = []
            if isinstance(self.sort_by, Sort):
                order.append(self.sort_by.query())
            elif isinstance(self.sort_by, list):
                order = [s.query() for s in self.sort_by]
            req.sort = marshal(order)
        if self.group_by:
            g = [self.group_by] if isinstance(self.group_by, str) else self.group_by
            req.group_by = marshal(g)
        if self.include_fields:
            req.include_fields.extend(self.include_fields)
        if self.exclude_fields:
            req.exclude_fields.extend(self.exclude_fields)
        req.page_size = self.hits_per_page


# Search result fields


@dataclass
class DocStatus:
    id: str = None
    error: Optional[TigrisException] = None
    _p: InitVar[ProtoDocStatus] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoDocStatus):
        if _p:
            if _p.HasField("error"):
                self.error = TigrisException(_p.error.message)
            if _p.id:
                self.id = _p.id


@dataclass
class TextMatchInfo:
    score: Optional[str] = None
    vector_distance: Optional[float] = None
    fields: List[str] = field(default_factory=list)
    _p: InitVar[ProtoMatch] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoMatch):
        if _p:
            self.fields = [f.name for f in _p.fields]
            if _p.HasField("vector_distance"):
                self.vector_distance = _p.vector_distance
            if _p.score:
                self.score = _p.score


@dataclass
class DocMeta:
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    text_match: TextMatchInfo = field(default_factory=TextMatchInfo)
    _p: InitVar[ProtoSearchHitMeta] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchHitMeta):
        if _p:
            if _p.HasField("created_at"):
                self.created_at = _p.created_at.ToDatetime(tzinfo=timezone.utc)
            if _p.HasField("updated_at"):
                self.updated_at = _p.updated_at.ToDatetime(tzinfo=timezone.utc)
            if _p.HasField("match"):
                self.text_match = TextMatchInfo(_p=_p.match)


@dataclass
class IndexedDoc:
    doc: Optional[Document] = None
    meta: DocMeta = field(default_factory=DocMeta)
    _p: InitVar[ProtoSearchHit] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchHit):
        if _p:
            if _p.data:
                self.doc = unmarshal(_p.data)
            if _p.HasField("metadata"):
                self.meta = DocMeta(_p=_p.metadata)


@dataclass
class GroupedHits:
    keys: [str] = field(default_factory=list)
    hits: [IndexedDoc] = field(default_factory=list)
    _p: InitVar[ProtoGroupedHits] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoGroupedHits):
        if _p:
            self.keys = _p.group_keys
            self.hits = [IndexedDoc(_p=h) for h in _p.hits]


@dataclass
class FacetCount:
    value: Optional[str] = None
    count: Optional[int] = None
    _p: InitVar[ProtoFacetCount] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoFacetCount):
        if _p:
            self.value = _p.value
            self.count = _p.count


@dataclass
class FacetStats:
    count: int = 0
    sum: Optional[float] = None
    avg: Optional[float] = None
    max: Optional[float] = None
    min: Optional[float] = None
    _p: InitVar[ProtoFacetStats] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoFacetStats):
        if _p:
            self.count = _p.count
            if _p.HasField("sum"):
                self.sum = _p.sum
            if _p.HasField("avg"):
                self.avg = _p.avg
            if _p.HasField("max"):
                self.max = _p.max
            if _p.HasField("min"):
                self.min = _p.min


@dataclass
class Facets:
    counts: [FacetCount] = field(default_factory=list)
    stats: FacetStats = field(default_factory=FacetStats)
    _p: InitVar[ProtoSearchFacet] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchFacet):
        if _p:
            if _p.HasField("stats"):
                self.stats = FacetStats(_p=_p.stats)
            self.counts = [FacetCount(_p=fc) for fc in _p.counts]


@dataclass
class Page:
    current: int = 1
    size: int = 20
    _p: InitVar[ProtoPage] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoPage):
        if _p:
            if _p.current:
                self.current = _p.current
            self.size = _p.size


@dataclass
class Meta:
    found: int = 0
    total_pages: int = 1
    page: Page = field(default_factory=Page)
    _p: InitVar[ProtoSearchMeta] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchMeta):
        if _p:
            if _p.HasField("page"):
                self.page = Page(_p=_p.page)
            self.found = _p.found
            if _p.total_pages:
                self.total_pages = _p.total_pages


@dataclass
class Result:
    hits: List[IndexedDoc] = field(default_factory=list)
    facets: Dict[str, Facets] = field(default_factory=dict)
    meta: Meta = field(default_factory=Meta)
    grouped_hits: [GroupedHits] = field(default_factory=list)
    _p: InitVar[ProtoSearchIndexResponse] = dataclass_default_proto_field

    def __post_init__(self, _p: ProtoSearchIndexResponse):
        if _p:
            self.hits = [IndexedDoc(_p=h) for h in _p.hits]
            self.grouped_hits = [GroupedHits(_p=g) for g in _p.group]
            self.facets = {k: Facets(_p=v) for k, v in _p.facets.items()}
            if _p.HasField("meta"):
                self.meta = Meta(_p=_p.meta)
