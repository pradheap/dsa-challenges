import unittest

from challenges.string.source.longest_common_palindromic_subsequence import longest_common_palindromic_subsequence


class TestLongestCommonPalindromicSubstring(unittest.TestCase):

    def test_longest_common_palindromic_subsequence_dp(self):
        self.assertEqual('abdba', longest_common_palindromic_subsequence('afbdba'))
        self.assertEqual('tacocat', longest_common_palindromic_subsequence('tacocats'))
        self.assertEqual('tacocat', longest_common_palindromic_subsequence('tdafcocsaht'))
        self.assertEqual('tacocattacocat', longest_common_palindromic_subsequence('tacocattacocat'))
        self.assertEqual('abba', longest_common_palindromic_subsequence('abba'))
        self.assertEqual('abba', longest_common_palindromic_subsequence('abbas'))
        self.assertEqual('aba', longest_common_palindromic_subsequence('aba'))
        self.assertEqual('aba', longest_common_palindromic_subsequence('abca'))
        self.assertEqual('abcba', longest_common_palindromic_subsequence('abcba'))
        self.assertEqual('abcba', longest_common_palindromic_subsequence('abcbadd'))