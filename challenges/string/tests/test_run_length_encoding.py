import unittest

from challenges.string.source.run_length_encoding import run_length_encoding


class TestRLEncoding(unittest.TestCase):

    def test_run_length_encoding(self):
        ip = 'AAABGGGFF'
        exp = 'A3B1G3F2'
        self.assertEqual(exp, run_length_encoding(ip))

        ip = 'WWWWWWEEEECDOOOODFFFFJJJJJJJJJJQQQQQQQZ'
        exp = 'W6E4C1D1O4D1F4J10Q7Z1'
        self.assertEqual(exp, run_length_encoding(ip))