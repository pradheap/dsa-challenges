import unittest

from lib.source.disjointset import *

class TestDisjointSet(unittest.TestCase):
    def test_disjointset(self):
        djs = DisjointSet()
        for i in ['a', 'b', 'c', 'd', 'e', 'f']:
            djs.make_set(i)
        djs.merge_set('a', 'b')
        djs.merge_set('c', 'd')
        djs.merge_set('c', 'e')
        djs.merge_set('e', 'f')
        self.assertEqual(djs.find_set('a'), 'b')
        self.assertEqual(djs.find_set('b'), 'b')
        self.assertEqual(djs.find_set('f'), 'd')
        self.assertEqual(djs.find_set('e'), 'd')
        djs.merge_set('b', 'f')
        self.assertEqual(djs.find_set('b'), 'd')