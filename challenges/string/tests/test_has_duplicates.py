import unittest
from challenges.string.source.has_duplicates import has_duplicates, has_duplicates_v1


class TestHasDuplicates(unittest.TestCase):

    def test_has_duplicates(self):
        self.assertEqual(False, has_duplicates("adfcghkporew"))
        self.assertEqual(True, has_duplicates("adfcadfg"))

        self.assertEqual(False, has_duplicates_v1("adfcghkporew"))
        self.assertEqual(True, has_duplicates_v1("adfcadfg"))