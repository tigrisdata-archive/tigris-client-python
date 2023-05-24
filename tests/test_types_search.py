from datetime import datetime
from unittest import TestCase

from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp

from api.generated.server.v1.api_pb2 import FacetCount as ProtoFacetCount
from api.generated.server.v1.api_pb2 import FacetStats as ProtoFacetStats
from api.generated.server.v1.api_pb2 import GroupedSearchHits as ProtoGroupedHits
from api.generated.server.v1.api_pb2 import Match as ProtoMatch
from api.generated.server.v1.api_pb2 import MatchField as ProtoMatchField
from api.generated.server.v1.api_pb2 import Page as ProtoPage
from api.generated.server.v1.api_pb2 import SearchFacet as ProtoSearchFacet
from api.generated.server.v1.api_pb2 import SearchHit as ProtoSearchHit
from api.generated.server.v1.api_pb2 import SearchHitMeta as ProtoSearchHitMeta
from api.generated.server.v1.api_pb2 import SearchMetadata as ProtoSearchMeta
from api.generated.server.v1.observability_pb2 import Error as ProtoError
from api.generated.server.v1.search_pb2 import DocStatus as ProtoDocStatus
from api.generated.server.v1.search_pb2 import SearchIndexRequest
from api.generated.server.v1.search_pb2 import (
    SearchIndexResponse as ProtoSearchIndexResponse,
)
from tigrisdb.errors import TigrisException
from tigrisdb.types import sort
from tigrisdb.types.filters import LT, And, Eq
from tigrisdb.types.search import (
    DocMeta,
    DocStatus,
    FacetCount,
    Facets,
    FacetSize,
    FacetStats,
    GroupedHits,
    IndexedDoc,
    Meta,
    Page,
    Query,
    Result,
    TextMatchInfo,
    VectorField,
)
from tigrisdb.utils import marshal


class SearchQueryTest(TestCase):
    def test_default_fields(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.__build__(proto_req)

        self.assertEqual(proto_req.q, "")
        self.assertEqual(proto_req.search_fields, [])
        self.assertEqual(proto_req.vector, bytearray())
        self.assertEqual(proto_req.filter, bytearray())
        self.assertEqual(proto_req.facet, bytearray())
        self.assertEqual(proto_req.sort, bytearray())
        self.assertEqual(proto_req.group_by, bytearray())
        self.assertEqual(proto_req.include_fields, [])
        self.assertEqual(proto_req.exclude_fields, [])
        self.assertEqual(proto_req.page_size, 20)

    def test_with_q(self):
        query, proto_req = Query(q="hello world"), SearchIndexRequest()
        query.__build__(proto_req)

        self.assertEqual("hello world", proto_req.q)

    def test_with_search_fields(self):
        query, proto_req = (
            Query(search_fields=["name.first", "balance"]),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)

        self.assertEqual(["name.first", "balance"], proto_req.search_fields)

    def test_with_vector_query(self):
        query, proto_req = (
            Query(vector_query=VectorField("embedding", [1.1, 2.456, 34.88])),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)

        self.assertEqual(
            '{"embedding": [1.1, 2.456, 34.88]}'.encode(), proto_req.vector
        )

    def test_with_filter_by(self):
        query, proto_req = (
            Query(
                filter_by=And(
                    Eq("name", "Alex"),
                    LT("dob", datetime.fromisoformat("2023-05-05T10:00:00+00:00")),
                )
            ),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)
        self.assertEqual(
            '{"$and": ['
            '{"name": "Alex"}, '
            '{"dob": {"$lt": "2023-05-05T10:00:00+00:00"}}'
            "]}".encode(),
            proto_req.filter,
        )

    def test_with_facet_by(self):
        query, proto_req = Query(facet_by="field_1"), SearchIndexRequest()
        query.__build__(proto_req)
        self.assertEqual(
            '{"field_1": {"size": 10, "type": "value"}}'.encode(), proto_req.facet
        )

        query, proto_req = (
            Query(facet_by=["f1", FacetSize("f2", 25), FacetSize("f3")]),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)
        self.assertEqual(
            '{"f1": {"size": 10, "type": "value"}, "f2": {"size": 25, "type": "value"},'
            ' "f3": {"size": 10, "type": "value"}}'.encode(),
            proto_req.facet,
        )

    def test_with_sort_by(self):
        query, proto_req = Query(sort_by=sort.Ascending("f1")), SearchIndexRequest()
        query.__build__(proto_req)
        self.assertEqual('[{"f1": "$asc"}]'.encode(), proto_req.sort)

        query, proto_req = (
            Query(
                sort_by=[
                    sort.Descending("f2"),
                    sort.Ascending("f1"),
                    sort.Ascending("f3"),
                ]
            ),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)
        self.assertEqual(
            '[{"f2": "$desc"}, {"f1": "$asc"}, {"f3": "$asc"}]'.encode(), proto_req.sort
        )

    def test_with_group_by(self):
        query, proto_req = Query(group_by="f1"), SearchIndexRequest()
        query.__build__(proto_req)
        self.assertEqual('["f1"]'.encode(), proto_req.group_by)

        query, proto_req = Query(group_by=["f1", "f2", "f3"]), SearchIndexRequest()
        query.__build__(proto_req)
        self.assertEqual('["f1", "f2", "f3"]'.encode(), proto_req.group_by)

    def test_with_include_fields(self):
        query, proto_req = (
            Query(include_fields=["f1", "f2", "f3"]),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)
        self.assertEqual(["f1", "f2", "f3"], proto_req.include_fields)

    def test_with_exclude_fields(self):
        query, proto_req = (
            Query(exclude_fields=["f1", "f2", "f3"]),
            SearchIndexRequest(),
        )
        query.__build__(proto_req)
        self.assertEqual(["f1", "f2", "f3"], proto_req.exclude_fields)

    def test_with_page_size(self):
        query, proto_req = Query(hits_per_page=25), SearchIndexRequest()
        query.__build__(proto_req)
        self.assertEqual(25, proto_req.page_size)


class SearchResultTestCase(TestCase):
    def test_build_doc_status(self):
        cases = [
            (
                "with empty msg",
                ProtoDocStatus(id="1", error=ProtoError(message="failure")),
                DocStatus(id="1", error=TigrisException("failure")),
            ),
            ("with empty msg", ProtoDocStatus(), DocStatus(id=None, error=None)),
            ("with None", None, DocStatus(id=None, error=None)),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = DocStatus(_p=proto_msg)
                self.assertEqual(expected.id, actual.id)
                if expected.error:
                    self.assertIsNotNone(actual.error)
                    self.assertEqual(proto_msg.error.message, actual.error.msg)

    def test_build_text_match_info(self):
        cases = [
            (
                "with complete msg",
                ProtoMatch(
                    score="25",
                    vector_distance=45.1,
                    fields=[ProtoMatchField(name="f1")],
                ),
                TextMatchInfo(score="25", vector_distance=45.1, fields=["f1"]),
            ),
            (
                "with empty msg",
                ProtoMatch(),
                TextMatchInfo(score=None, vector_distance=None, fields=[]),
            ),
            (
                "with None",
                None,
                TextMatchInfo(score=None, vector_distance=None, fields=[]),
            ),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = TextMatchInfo(_p=proto_msg)
                self.assertEqual(expected.score, actual.score)
                self.assertEqual(expected.vector_distance, actual.vector_distance)
                self.assertEqual(expected.fields, actual.fields)

    def test_build_doc_meta(self):
        ts, proto_ts = (
            datetime.fromisoformat("2023-05-05T10:00:00+00:00"),
            ProtoTimestamp(),
        )
        proto_ts.FromDatetime(ts)
        cases = [
            (
                "with complete msg",
                ProtoSearchHitMeta(created_at=proto_ts, updated_at=proto_ts),
                DocMeta(created_at=ts, updated_at=ts, text_match=TextMatchInfo()),
            ),
            (
                "with empty msg",
                ProtoSearchHitMeta(),
                DocMeta(created_at=None, updated_at=None, text_match=TextMatchInfo()),
            ),
            (
                "with None",
                None,
                DocMeta(created_at=None, updated_at=None, text_match=TextMatchInfo()),
            ),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = DocMeta(_p=proto_msg)
                self.assertEqual(expected.created_at, actual.created_at)
                self.assertEqual(expected.updated_at, actual.updated_at)
                self.assertEqual(expected.text_match, actual.text_match)

    def test_build_indexed_doc(self):
        cases = [
            (
                "with complete msg",
                ProtoSearchHit(data=marshal({"f": "v"}), metadata=ProtoSearchHitMeta()),
                IndexedDoc(doc={"f": "v"}, meta=DocMeta()),
            ),
            ("with empty msg", ProtoSearchHit(), IndexedDoc(doc=None, meta=DocMeta())),
            ("with None", None, IndexedDoc(doc=None, meta=DocMeta())),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = IndexedDoc(_p=proto_msg)
                self.assertEqual(actual.doc, expected.doc)
                self.assertEqual(actual.meta, expected.meta)

    def test_build_grouped_hits(self):
        cases = [
            (
                "with complete msg",
                ProtoGroupedHits(
                    group_keys=["f1"], hits=[ProtoSearchHit(data=marshal({"f": "v"}))]
                ),
                GroupedHits(keys=["f1"], hits=[IndexedDoc(doc={"f": "v"})]),
            ),
            ("with empty msg", ProtoGroupedHits(), GroupedHits(keys=[], hits=[])),
            ("with None", None, GroupedHits(keys=[], hits=[])),
        ]

        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = GroupedHits(_p=proto_msg)
                self.assertEqual(actual.keys, expected.keys)
                self.assertEqual(actual.hits, expected.hits)

    def test_build_facet_count(self):
        cases = [
            (
                "with complete msg",
                ProtoFacetCount(value="v1", count=5),
                FacetCount(count=5, value="v1"),
            ),
            ("with empty msg", ProtoFacetCount(), FacetCount(count=0, value="")),
            ("with None", None, FacetCount(count=None, value=None)),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = FacetCount(_p=proto_msg)
                self.assertEqual(expected.count, actual.count)
                self.assertEqual(expected.value, actual.value)

    def test_build_facet_stats(self):
        cases = [
            (
                "with complete msg",
                ProtoFacetStats(count=12, sum=8.5, avg=3.14, max=12, min=-1.9),
                FacetStats(count=12, sum=8.5, avg=3.14, max=12, min=-1.9),
            ),
            (
                "with empty msg",
                ProtoFacetStats(),
                FacetStats(count=0, sum=None, avg=None, max=None, min=None),
            ),
            (
                "with None",
                None,
                FacetStats(count=0, sum=None, avg=None, max=None, min=None),
            ),
            (
                "with missing count and avg",
                ProtoFacetStats(sum=8.5, max=12, min=-1.9),
                FacetStats(count=0, sum=8.5, avg=None, max=12, min=-1.9),
            ),
            (
                "with zero values",
                ProtoFacetStats(count=0, sum=0, avg=0, max=0, min=-0),
                FacetStats(count=0, sum=0, avg=0, max=0, min=0),
            ),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = FacetStats(_p=proto_msg)
                self.assertEqual(expected.count, actual.count)
                self.assertEqual(expected.sum, actual.sum)
                self.assertEqual(expected.avg, actual.avg)
                self.assertEqual(expected.max, actual.max)
                self.assertEqual(expected.min, actual.min)

    def test_build_facets(self):
        cases = [
            (
                "with complete msg",
                ProtoSearchFacet(
                    counts=[ProtoFacetCount(value="v1", count=2)],
                    stats=ProtoFacetStats(),
                ),
                Facets(counts=[FacetCount("v1", 2)], stats=FacetStats()),
            ),
            (
                "with empty msg",
                ProtoSearchFacet(),
                Facets(counts=[], stats=FacetStats()),
            ),
            ("with None", None, Facets(counts=[], stats=FacetStats())),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = Facets(_p=proto_msg)
                self.assertEqual(expected.counts, actual.counts)
                self.assertEqual(expected.stats, actual.stats)

    def test_build_page(self):
        cases = [
            (
                "with complete msg",
                ProtoPage(current=3, size=20),
                Page(current=3, size=20),
            ),
            ("with empty msg", ProtoPage(), Page(current=1, size=0)),
            ("with None", None, Page(current=1, size=20)),
            ("with partial msg", ProtoPage(size=10), Page(current=1, size=10)),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = Page(_p=proto_msg)
                self.assertEqual(expected.current, actual.current)
                self.assertEqual(expected.size, actual.size)

    def test_build_meta(self):
        cases = [
            (
                "with complete msg",
                ProtoSearchMeta(found=25, total_pages=3, page=ProtoPage()),
                Meta(found=25, total_pages=3, page=Page(_p=ProtoPage())),
            ),
            ("with None", None, Meta(found=0, total_pages=1, page=Page())),
            ("with empty msg", ProtoSearchMeta(), Meta(found=0, total_pages=1)),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = Meta(_p=proto_msg)
                # if proto_msg and proto_msg.HasField("page"):
                self.assertEqual(expected.page, actual.page)
                self.assertEqual(expected.total_pages, actual.total_pages)
                self.assertEqual(expected.found, actual.found)

    def test_build_result(self):
        cases = [
            (
                "with complete msg",
                ProtoSearchIndexResponse(
                    hits=[ProtoSearchHit(data=marshal({"f": "v"}))],
                    facets={"f1": ProtoSearchFacet()},
                    meta=ProtoSearchMeta(found=25, total_pages=3),
                    group=[
                        ProtoGroupedHits(
                            group_keys=["f1"],
                            hits=[ProtoSearchHit(data=marshal({"f": "v"}))],
                        )
                    ],
                ),
                Result(
                    hits=[IndexedDoc(doc={"f": "v"})],
                    facets={"f1": Facets()},
                    meta=Meta(found=25, total_pages=3),
                    grouped_hits=[
                        GroupedHits(keys=["f1"], hits=[IndexedDoc(doc={"f": "v"})])
                    ],
                ),
            ),
            (
                "with empty msg",
                ProtoSearchIndexResponse(),
                Result(hits=[], facets={}, meta=Meta(), grouped_hits=[]),
            ),
            (
                "with None",
                None,
                Result(hits=[], facets={}, meta=Meta(), grouped_hits=[]),
            ),
        ]
        for tc, proto_msg, expected in cases:
            with self.subTest(tc):
                actual = Result(_p=proto_msg)
                self.assertEqual(expected.hits, actual.hits)
                self.assertEqual(expected.meta, actual.meta)
                self.assertEqual(expected.facets, actual.facets)
                self.assertEqual(expected.grouped_hits, actual.grouped_hits)
