import unittest

from challenges.string.source.string_matching import naive_string_matching, rabin_karp_string_matching


class TestStringMatching(unittest.TestCase):
    def test_naive_string_matching(self):
        self.assertEqual(0, naive_string_matching('abacd', 'a'))
        self.assertEqual(4, naive_string_matching('abcde', 'e'))
        self.assertEqual(7, naive_string_matching('abcabcdabcde', 'abcde'))
        self.assertEqual(2, naive_string_matching('abcdef', 'cd'))
        self.assertEqual(4, naive_string_matching('abcdeffedbc', 'effe'))
        self.assertEqual(4, naive_string_matching('abcdef fedbc', 'ef fe'))

        self.assertEqual(0, rabin_karp_string_matching('abacd', 'a'))
        self.assertEqual(4, rabin_karp_string_matching('abcde', 'e'))
        self.assertEqual(7, rabin_karp_string_matching('abcabcdabcde', 'abcde'))
        self.assertEqual(2, rabin_karp_string_matching('abcdef', 'cd'))
        self.assertEqual(4, rabin_karp_string_matching('abcdeffedbc', 'effe'))
        self.assertEqual(4, rabin_karp_string_matching('abcdef fedbc', 'ef fe'))
