import unittest

from challenges.string.source.min_edit_distance import min_edit_distance


class TestMinimumEditDistance(unittest.TestCase):

    def test_min_edit_distance(self):
        self.assertEqual(2, min_edit_distance('abcde', 'abced'))
        self.assertEqual(1, min_edit_distance('abcde', 'abce'))
        self.assertEqual(0, min_edit_distance('abcde', 'abcde'))
        self.assertEqual(2, min_edit_distance('abcude', 'abced'))
        self.assertEqual(1, min_edit_distance('hello world', 'helloworld'))
        self.assertEqual(5, min_edit_distance('how are you', 'ho war eyo u'))
        self.assertEqual(9, min_edit_distance('you how are ', 'ho war eyo u'))