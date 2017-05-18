import unittest

from challenges.string.source.longest_common_subsequence import longest_common_subsequence_dp


class TestLongestCommonSubstring(unittest.TestCase):

    def test_longest_common_subsequence_dp(self):
        s1 = "birsdysdasdnsdi"
        s2 = "ptyertayuinuiip"
        exp = "yani"
        self.assertEqual(exp, longest_common_subsequence_dp(s1, s2))
        s1 = "zxabcdezy"
        s2 = "yzabcdezx"
        exp = "zabcdez"
        self.assertEqual(exp, longest_common_subsequence_dp(s1, s2))
        s1 = "XMJYAUZ"
        s2 = "MZJAWXU"
        exp = "MJAU"
        self.assertEqual(exp, longest_common_subsequence_dp(s1, s2))
        s1 = "nematodeknowledge"
        s2 = "emptybottle"
        exp = "emtole"
        self.assertEqual(exp, longest_common_subsequence_dp(s1, s2))