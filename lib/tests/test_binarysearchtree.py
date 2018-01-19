import unittest

from lib.source.binarysearchtree import BinarySearchTree
from challenges.datastructures.tree.source.traversals import in_order


class TestBST(unittest.TestCase):

    @staticmethod
    def create_bst():
        bst_tree = BinarySearchTree()
        bst_tree.insert(10)
        bst_tree.insert(6)
        bst_tree.insert(15)
        bst_tree.insert(11)
        bst_tree.insert(1)
        bst_tree.insert(4)
        bst_tree.insert(5)
        bst_tree.insert(9)
        bst_tree.insert(8)
        bst_tree.insert(3)
        bst_tree.insert(18)
        return bst_tree

    def test_bst_insert(self):
        bst_tree = self.create_bst()
        self.assertListEqual([1, 3, 4, 5, 6, 8, 9, 10, 11, 15, 18], in_order(bst_tree.get_root()))

    def test_bst_get(self):
        bst_tree = self.create_bst()
        self.assertIsNotNone(bst_tree.get(11))
        self.assertIsNotNone(bst_tree.get(1))
        self.assertIsNotNone(bst_tree.get(10))
        self.assertIsNone(bst_tree.get(101))
        self.assertIsNone(bst_tree.get(7))

    def test_bst_delete(self):
        bst_tree = BinarySearchTree()
        bst_tree.insert(10)
        bst_tree.insert(6)
        bst_tree.insert(4)
        bst_tree.insert(7)
        bst_tree.insert(9)
        bst_tree.insert(17)
        bst_tree.insert(13)
        bst_tree.insert(15)
        bst_tree.insert(21)
        self.assertListEqual([4, 6, 7, 9, 10, 13, 15, 17, 21], in_order(bst_tree.get_root()))
        self.assertIsNotNone(bst_tree.delete(6))
        self.assertIsNotNone(bst_tree.delete(7))
        self.assertListEqual([4, 9, 10, 13, 15, 17, 21], in_order(bst_tree.get_root()))
        self.assertIsNotNone(bst_tree.delete(17))
        self.assertIsNotNone(bst_tree.delete(4))
        self.assertListEqual([9, 10, 13, 15, 21], in_order(bst_tree.get_root()))
