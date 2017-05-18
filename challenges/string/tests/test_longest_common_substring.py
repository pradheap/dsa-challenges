import unittest

from challenges.string.source.longest_common_substring import common_substring_dp


class TestLongestCommonSubstring(unittest.TestCase):

    def test_longest_common_substring_dp(self):
        s1 = "biryani"
        s2 = "yanip"
        exp = "yani"
        self.assertEqual(exp, common_substring_dp(s1, s2))
        s1 = "zxabcdezy"
        s2 = "yzabcdezx"
        exp = "abcdez"
        self.assertEqual(exp, common_substring_dp(s1, s2))
        s1 = "courthouses"
        s2 = "housescourt"
        exp = "houses"
        self.assertEqual(exp, common_substring_dp(s1, s2))

