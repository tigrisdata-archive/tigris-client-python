import datetime
from unittest import TestCase

from tigrisdb.types import RFC3339_format
from tigrisdb.types.filters import GT, GTE, LT, LTE, Contains, Eq, Not, Regex


class SelectorTestCase(TestCase):
    def test_equals(self):
        f = Eq("f1", 25)
        self.assertEqual({"f1": 25}, f.query())

    def test_gte(self):
        f = GTE("f1", 25)
        self.assertEqual({"f1": {"$gte": 25}}, f.query())

    def test_gt(self):
        dt = datetime.datetime.strptime("2023-05-05T10:00:00+00:00", RFC3339_format)
        f = GT("f1", dt)
        self.assertEqual({"f1": {"$gt": dt}}, f.query())

    def test_lte(self):
        f = LTE("f1", 25)
        self.assertEqual({"f1": {"$lte": 25}}, f.query())

    def test_lt(self):
        f = LT("f1", 25)
        self.assertEqual({"f1": {"$lt": 25}}, f.query())

    def test_regex(self):
        f = Regex("f1", "emma*")
        self.assertEqual({"f1": {"$regex": "emma*"}}, f.query())

    def test_contains(self):
        f = Contains("f1", "cars")
        self.assertEqual({"f1": {"$contains": "cars"}}, f.query())

    def test_not(self):
        f = Not("f1", "Alex")
        self.assertEqual({"f1": {"$not": "Alex"}}, f.query())
