from unittest import TestCase

from tigrisdb.types.filters import GT, GTE, LTE, And, Contains, Eq, Not, Or, Regex


class LogicalFiltersTest(TestCase):
    def test_or(self):
        f = Or(Eq("f1", True), LTE("f2", 25), Contains("f3", "v1"))
        self.assertEqual(
            {"$or": [{"f1": True}, {"f2": {"$lte": 25}}, {"f3": {"$contains": "v1"}}]},
            f.query(),
        )

    def test_and(self):
        f = And(Eq("f1", True), LTE("f2", 25), Contains("f3", "v1"))
        self.assertEqual(
            {"$and": [{"f1": True}, {"f2": {"$lte": 25}}, {"f3": {"$contains": "v1"}}]},
            f.query(),
        )

    def test_empty(self):
        self.assertEqual({}, And().query())
        self.assertEqual({}, Or().query())

    def test_single(self):
        self.assertEqual({"f1": {"$gt": 10.5}}, Or(GT("f1", 10.5)).query())

    def test_complex_or_filter(self):
        f = Or(
            Or(Eq("name", "alice"), GTE("rank", 2)),
            Or(Eq("name", "emma"), LTE("rank", 6), Not("city", "sfo")),
            And(GTE("f1", 1.5), LTE("f1", 3.14), Contains("f2", "hello")),
            Not("f3", False),
            Regex("f4", "/andy/i"),
        )
        self.assertEqual(
            {
                "$or": [
                    {"$or": [{"name": "alice"}, {"rank": {"$gte": 2}}]},
                    {
                        "$or": [
                            {"name": "emma"},
                            {"rank": {"$lte": 6}},
                            {"city": {"$not": "sfo"}},
                        ]
                    },
                    {
                        "$and": [
                            {"f1": {"$gte": 1.5}},
                            {"f1": {"$lte": 3.14}},
                            {"f2": {"$contains": "hello"}},
                        ]
                    },
                    {"f3": {"$not": False}},
                    {"f4": {"$regex": "/andy/i"}},
                ]
            },
            f.query(),
        )

    def test_complex_and_filter(self):
        f = And(
            Or(Eq("name", "alice"), GTE("rank", 2)),
            Or(Eq("name", "emma"), LTE("rank", 6), Not("city", "sfo")),
        )

        self.assertEqual(
            {
                "$and": [
                    {"$or": [{"name": "alice"}, {"rank": {"$gte": 2}}]},
                    {
                        "$or": [
                            {"name": "emma"},
                            {"rank": {"$lte": 6}},
                            {"city": {"$not": "sfo"}},
                        ]
                    },
                ]
            },
            f.query(),
        )
