import unittest
from challenges.string.source.reverse_string import reverse_string, reverse_string_v1


class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        ip = 'strong'
        exp = 'gnorts'
        self.assertEqual(exp, reverse_string(ip))

        ip = 'tacocat'
        exp = 'tacocat'
        self.assertEqual(exp, reverse_string(ip))

        ip = 'strong'
        exp = 'gnorts'
        self.assertEqual(exp, reverse_string_v1(ip))

        ip = 'tacocat'
        exp = 'tacocat'
        self.assertEqual(exp, reverse_string_v1(ip))