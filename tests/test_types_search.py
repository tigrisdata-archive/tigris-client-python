from unittest import TestCase

from api.generated.server.v1.search_pb2 import SearchIndexRequest
from tigrisdb.types import sort
from tigrisdb.types.search import FacetSize, Query, VectorField


class SearchQueryTest(TestCase):
    def test_default_fields(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.__build__(proto_req)

        self.assertEqual(proto_req.q, "")
        self.assertEqual(proto_req.search_fields, [])
        self.assertEqual(proto_req.vector, bytearray())
        self.assertEqual(proto_req.facet, bytearray())
        self.assertEqual(proto_req.sort, bytearray())
        self.assertEqual(proto_req.group_by, bytearray())
        self.assertEqual(proto_req.include_fields, [])
        self.assertEqual(proto_req.exclude_fields, [])
        self.assertEqual(proto_req.page_size, 20)

    def test_with_q(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.q = "hello world"
        query.__build__(proto_req)

        self.assertEqual("hello world", proto_req.q)

    def test_with_search_fields(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.search_fields = ["name.first", "balance"]
        query.__build__(proto_req)

        self.assertEqual(["name.first", "balance"], proto_req.search_fields)

    def test_with_vector_query(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.vector_query = VectorField("embedding", [1.1, 2.456, 34.88])
        query.__build__(proto_req)

        self.assertEqual(
            '{"embedding": [1.1, 2.456, 34.88]}'.encode(), proto_req.vector
        )

    def test_with_facet_by(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.facet_by = "field_1"
        query.__build__(proto_req)
        self.assertEqual(
            '{"field_1": {"size": 10, "type": "value"}}'.encode(), proto_req.facet
        )

        query, proto_req = Query(), SearchIndexRequest()
        query.facet_by = ["f1", FacetSize("f2", 25), FacetSize("f3")]
        query.__build__(proto_req)
        self.assertEqual(
            '{"f1": {"size": 10, "type": "value"}, "f2": {"size": 25, "type": "value"},'
            ' "f3": {"size": 10, "type": "value"}}'.encode(),
            proto_req.facet,
        )

    def test_with_sort_by(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.sort_by = sort.Ascending("f1")
        query.__build__(proto_req)
        self.assertEqual('[{"f1": "$asc"}]'.encode(), proto_req.sort)

        query, proto_req = Query(), SearchIndexRequest()
        query.sort_by = [
            sort.Descending("f2"),
            sort.Ascending("f1"),
            sort.Ascending("f3"),
        ]
        query.__build__(proto_req)
        self.assertEqual(
            '[{"f2": "$desc"}, {"f1": "$asc"}, {"f3": "$asc"}]'.encode(), proto_req.sort
        )

    def test_with_group_by(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.group_by = "f1"
        query.__build__(proto_req)
        self.assertEqual('["f1"]'.encode(), proto_req.group_by)

        query, proto_req = Query(), SearchIndexRequest()
        query.group_by = ["f1", "f2", "f3"]
        query.__build__(proto_req)
        self.assertEqual('["f1", "f2", "f3"]'.encode(), proto_req.group_by)

    def test_with_include_fields(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.include_fields = ["f1", "f2", "f3"]
        query.__build__(proto_req)
        self.assertEqual(["f1", "f2", "f3"], proto_req.include_fields)

    def test_with_exclude_fields(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.exclude_fields = ["f1", "f2", "f3"]
        query.__build__(proto_req)
        self.assertEqual(["f1", "f2", "f3"], proto_req.exclude_fields)

    def test_with_page_size(self):
        query, proto_req = Query(), SearchIndexRequest()
        query.hits_per_page = 25
        query.__build__(proto_req)
        self.assertEqual(25, proto_req.page_size)
