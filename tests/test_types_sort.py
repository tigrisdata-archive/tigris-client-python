from unittest import TestCase

from tigrisdb.types.sort import Ascending, Descending, Sort


class SortTests(TestCase):
    def test_ascending(self):
        sort = Ascending("f1")
        self.assertEqual({"f1": "$asc"}, sort.query())

    def test_descending(self):
        sort = Descending("f1")
        self.assertEqual({"f1": "$desc"}, sort.query())

    def test_base_sort_error(self):
        with self.assertRaisesRegex(TypeError, "abstract class"):
            Sort()
