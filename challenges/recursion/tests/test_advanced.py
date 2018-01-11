import unittest

from challenges.recursion.source.advanced import *

class TestAdvanced(unittest.TestCase):

    def test_group_sum(self):
        self.assertTrue(group_sum(0, [2, 4, 8], 10))
        self.assertTrue(group_sum(0, [2, 4, 8], 14))
        self.assertTrue(group_sum(0, [2, 4, 8], 8))
        self.assertTrue(group_sum(0, [2, 4, 8], 2))
        self.assertTrue(group_sum(2, [1, 2, 3, 4, 8, 1, 9], 5))
        self.assertTrue(group_sum(5, [1, 2, 3, 4, 8, 9], 9))
        self.assertFalse(group_sum(0, [2, 4, 8], 11))
        self.assertFalse(group_sum(0, [2, 4, 8], 9))
        self.assertFalse(group_sum(4, [1, 2, 3, 4, 8, 9], 5))
    
    def test_group_sum6(self):
        self.assertTrue(group_sum6(0, [2, 4, 8], 10))
        self.assertTrue(group_sum6(0, [3, 6, 8], 9))
        self.assertTrue(group_sum6(0, [6, 3, 6, 8], 12))
        self.assertTrue(group_sum6(0, [6, 6, 8], 12))
        self.assertFalse(group_sum6(0, [3, 3, 6], 3))
        self.assertFalse(group_sum6(0, [5, 6, 2], 7))
        self.assertFalse(group_sum6(0, [5, 6, 2, 6], 6))
    
    def test_group_no_adj(self):
        self.assertTrue(group_no_adj(0, [2, 10, 8, 10], 20))
        self.assertTrue(group_no_adj(0, [3, 6, 8], 11))
        self.assertTrue(group_no_adj(0, [6, 3, 6, 8], 11))
        self.assertTrue(group_no_adj(0, [6, 6, 8], 14))
        self.assertFalse(group_no_adj(0, [3, 6, 3], 9))
        self.assertFalse(group_no_adj(0, [5, 6, 2], 8))
        self.assertFalse(group_no_adj(0, [5, 6, 2, 6], 14))

    def test_group_sum_5(self):
        self.assertTrue(group_sum_5(0, [2, 5, 10, 4], 19))
        self.assertTrue(group_sum_5(0, [2, 5, 10, 4], 17))
        self.assertTrue(group_sum_5(0, [2, 5, 1, 4], 6))
        self.assertTrue(group_sum_5(0, [2, 5, 5, 1, 10, 20, 3], 38))
        self.assertTrue(group_sum_5(0, [2, 5, 2, 10, 20, 3], 38))
        self.assertFalse(group_sum_5(0, [2, 5, 2, 10, 20, 3], 33))
        self.assertFalse(group_sum_5(0, [2, 5, 1, 5, 1, 5], 10))
    
    def test_group_sum_clump(self):
        self.assertTrue(group_sum_clump(0, [2, 4, 8], 10))
        self.assertTrue(group_sum_clump(0, [2, 4, 1, 1, 1, 8], 9))
        self.assertTrue(group_sum_clump(0, [2, 4, 2, 2, 2, 8], 16))
        self.assertTrue(group_sum_clump(0, [2, 4, 11, 11, 44, 11, 11, 8], 44))
        self.assertTrue(group_sum_clump(0, [2, 4, 8, 8, 8], 30))
        self.assertFalse(group_sum_clump(0, [2, 2, 4, 8], 14))
        self.assertFalse(group_sum_clump(0, [2, 4, 4, 8], 12))
        self.assertFalse(group_sum_clump(0, [5, 4, 4, 4, 8], 16))
        self.assertFalse(group_sum_clump(0, [5, 1, 1, 1, 1], 7))
        self.assertFalse(group_sum_clump(0, [5, 1, 1, 1], 7))
        self.assertFalse(group_sum_clump(0, [2, 4, 4, 8], 14))
    
    def test_split_array(self):
        self.assertTrue(split_array([2, 2]))
        self.assertTrue(split_array([2, 0, 2]))
        self.assertTrue(split_array([4, 2, 2]))
        self.assertTrue(split_array([4, 4, 2, 2]))
        self.assertTrue(split_array([2, 2, 2, 2, 3, 5]))
        self.assertTrue(split_array([12, 2, 2, 2, 3, 5, 1, 1]))
        self.assertTrue(split_array([2, 2, 2, 4, 3, 1]))
        self.assertFalse(split_array([2, 1]))
        self.assertFalse(split_array([2, 1, 5]))
        self.assertFalse(split_array([2, 14]))
        self.assertFalse(split_array([2, 13, 17, 11]))
        self.assertFalse(split_array([2, 19, 100, 400, 500]))
    
    def test_split_odd_10(self):
        self.assertTrue(split_odd_10([5, 5, 5]))
        self.assertTrue(split_odd_10([5, 5, 1]))
        self.assertTrue(split_odd_10([5, 5, 6, 1]))
        self.assertTrue(split_odd_10([5, 5, 7, 6]))
        self.assertTrue(split_odd_10([55, 5, 15]))
        self.assertTrue(split_odd_10([55, 6, 15, 15]))
        self.assertTrue(split_odd_10([55, 15, 25]))
        self.assertFalse(split_odd_10([5, 5, 6]))
        self.assertFalse(split_odd_10([55, 5, 25, 1]))
        self.assertFalse(split_odd_10([5, 5, 5, 1]))
        self.assertFalse(split_odd_10([2, 5, 15]))
    
    def test_split_53(self):
        self.assertTrue(split_53([1,1]))
        self.assertTrue(split_53([2, 4, 2]))
        self.assertTrue(split_53([5, 5, 3, 3, 5, 3, 3, 3]))
        self.assertTrue(split_53([3, 3, 4, 1, 5, 5, 1]))
        self.assertTrue(split_53([1,1]))
        self.assertFalse(split_53([3, 3, 5, 5, 5, 1]))
        self.assertFalse(split_53([6, 7, 5, 5, 3]))
        self.assertFalse(split_53([3, 3, 3, 1, 5]))