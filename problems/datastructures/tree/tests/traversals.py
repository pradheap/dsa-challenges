import unittest

from lib.tree.source.binarytree import BinaryTree
from problems.datastructures.tree.source.traversals import *


class TestNode(unittest.TestCase):
    def test_pre_order(self):
        btree = BinaryTree('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = pre_order(btree)
        self.assertListEqual(result, ['1', '2', '3', '4', '5', '6', '7'])

    def test_post_order(self):
        btree = BinaryTree('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = post_order(btree)
        self.assertListEqual(result, ['3', '4', '2', '6', '7', '5', '1'])

    def test_in_order(self):
        btree = BinaryTree('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = in_order(btree)
        self.assertListEqual(result, ['3', '2', '4', '1', '6', '5', '7'])

    def test_get_height(self):
        btree = BinaryTree('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')
        result = get_height(btree)
        self.assertEqual(result, 4)

    def test_level_order(self):
        btree = BinaryTree('1')
        btree.insert_left('2')
        btree.insert_right('5')
        btree.get_left_child().insert_left('3')
        btree.get_left_child().insert_right('4')
        btree.get_right_child().insert_left('6')
        btree.get_right_child().insert_right('7')

        result = level_order(btree)
        self.assertListEqual(result, ['1', '2', '5', '3', '4', '6', '7'])