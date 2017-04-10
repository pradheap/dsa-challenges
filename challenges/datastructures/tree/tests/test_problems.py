import unittest

from lib.tree.source.binarytreenode import BinaryTreeNode

from challenges.datastructures.tree.source.problems import mirror_tree, is_identical, all_paths, bst_search
from challenges.datastructures.tree.source.traversals import pre_order, in_order


class TestProblems(unittest.TestCase):
    def test_mirror_tree(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')

        result = pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '4', '5', '6', '7'])
        mirror = pre_order(mirror_tree(btree))
        self.assertListEqual(mirror, ['1', '5', '7', '6', '2', '4', '3'])

    def test_is_identical(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')

        btree1 = BinaryTreeNode('1')
        btree1.insert_left('2')
        btree1.insert_right('5')
        btree1.get_left_child().insert_left('3')
        btree1.get_left_child().insert_right('4')
        btree1.get_right_child().insert_left('6')
        btree1.get_right_child().insert_right('7')

        self.assertTrue(is_identical(btree, btree1))

        btree2 = BinaryTreeNode('1')
        btree2.insert_left('2')
        btree2.insert_right('5')
        btree2.get_left_child().insert_left('3')
        btree2.get_left_child().insert_right('4')

        btree3 = BinaryTreeNode('1')
        btree3.insert_left('2')
        btree3.insert_right('5')
        btree3.get_left_child().insert_left('3')
        btree3.get_left_child().insert_right('4')
        btree3.get_right_child().insert_left('6')
        btree3.get_right_child().insert_right('7')

        self.assertFalse(is_identical(btree2, btree3))

        btree4 = BinaryTreeNode('1')
        btree4.insert_left('2')
        btree4.insert_right('5')
        btree4.get_left_child().insert_left('3')
        btree4.get_right_child().insert_right('7')

        btree5 = BinaryTreeNode('1')
        btree5.insert_left('2')
        btree5.insert_right('5')
        btree5.get_left_child().insert_right('4')
        btree5.get_right_child().insert_left('6')

        self.assertFalse(is_identical(btree4, btree5))

    def test_all_paths(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')

        result = pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '4', '5', '6', '7'])

        paths = all_paths(btree)
        self.assertListEqual(paths, [['1', '2', '3'], ['1', '2', '4'], ['1', '5', '6'], ['1', '5', '7']])

        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().get_left_child().insert_left('8')
        btree.get_left_child().insert_right('4')
        btree.get_left_child().get_right_child().insert_left('9')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')


        result = pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '8', '4', '9', '5', '6', '7'])

        paths = all_paths(btree)
        self.assertListEqual(paths, [['1', '2', '3', '8'], ['1', '2', '4','9'], ['1', '5', '6'], ['1', '5', '7']])

# Binary Search Tree Tests
    def test_bst_search(self):
        btree = BinaryTreeNode(5)
        btree.insert_left(3)
        btree.insert_right(7)
        btree.get_left_child().insert_left(2)
        btree.get_left_child().insert_right(4)
        btree.get_right_child().insert_left(6)
        btree.get_right_child().insert_right(9)
        self.assertListEqual(in_order(btree), [2, 3, 4, 5, 6, 7, 9])

        self.assertTrue(bst_search(btree, 6))
        self.assertFalse(bst_search(btree, 61))
