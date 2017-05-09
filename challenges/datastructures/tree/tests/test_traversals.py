import unittest

from lib.tree.source.binarytreenode import BinaryTreeNode
from challenges.datastructures.tree.source.traversals import *


class TestNode(unittest.TestCase):
    def test_pre_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '4', '5', '6', '7'])

    def test_post_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = post_order(btree)
        self.assertListEqual(result, ['3', '4', '2', '6', '7', '5', '1'])

    def test_in_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = in_order(btree)
        self.assertListEqual(result, ['3', '2', '4', '1', '6', '5', '7'])

    def test_level_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')

        result = level_order(btree)
        self.assertListEqual(result, ['1', '2', '5', '3', '4', '6', '7'])

    def test_reverse_level_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        btree.get_right_child().get_right_child().insert_left('9')
        btree.get_right_child().get_right_child().insert_right('12')

        result = reverse_level_order(btree)
        self.assertListEqual(result, ['9', '12', '3', '4', '6', '7', '2', '5', '1'])

    def test_zig_zag_level_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        btree.get_right_child().get_right_child().insert_left('9')
        btree.get_right_child().get_right_child().insert_right('12')

        result = zig_zag_level_order(btree)
        self.assertListEqual(result, ['1', '5', '2', '3', '4', '6', '7', '12', '9'])

    def test_iterative_pre_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = iterative_pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '4', '5', '6', '7'])

    def test_iterative_in_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_left_child().get_left_child().insert_right('8')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        btree.get_right_child().get_right_child().insert_left('9')
        result = iterative_in_order(btree)
        self.assertListEqual(result, ['3', '8', '2', '4', '1', '6', '5', '9', '7'])

    def test_iterative_post_order(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = iterative_post_order(btree)
        self.assertListEqual(result, ['3', '4', '2', '6', '7', '5', '1'])

    def test_iterative_post_order_two_stacks(self):
        btree = BinaryTreeNode('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = iterative_post_order_two_stacks(btree)
        self.assertListEqual(result, ['3', '4', '2', '6', '7', '5', '1'])