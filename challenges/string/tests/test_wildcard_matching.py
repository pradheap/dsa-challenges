import unittest

from challenges.string.source.wildcard_matching import wildcard_match


class TestWildcardMatching(unittest.TestCase):
    def test_wildcard_match(self):
        self.assertTrue(wildcard_match('dexter', 'd*r'))
        self.assertTrue(wildcard_match('dexter', 'd*x*r'))
        self.assertTrue(wildcard_match('dexter', 'd*e*r'))
        self.assertTrue(wildcard_match('dexter', 'd*t?r'))
        self.assertTrue(wildcard_match('dexter', 'd?*?r'))
        self.assertFalse(wildcard_match('dexter', 'd?t?r'))
        self.assertFalse(wildcard_match('dexter', 'd?x?r'))
        self.assertTrue(wildcard_match('dexter', 'd*er*'))
        self.assertTrue(wildcard_match('dexter', '?*ter*'))
        self.assertTrue(wildcard_match('dexter', 'd**r'))