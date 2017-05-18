# This Python file uses the following encoding: utf-8

import unittest

from challenges.string.source.is_anagram import is_anagram


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        s1 = "a1bc"
        s2 = "c1ba"
        self.assertEqual(True, is_anagram(s1, s2))

        s1 = "DropCote"
        s2 = "TopCoder"
        self.assertEqual(True, is_anagram(s1, s2))

        s1 = u"DropĈote"
        s2 = u"Topĉoder"
        self.assertEqual(True, is_anagram(s1, s2))