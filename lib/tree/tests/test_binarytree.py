import unittest

from lib.tree.source.binarytreenode import BinaryTreeNode


class TestNode(unittest.TestCase):
    def test_tree(self):
        btree = BinaryTreeNode('Sentence')
        btree.insert_left('Noun')
        btree.insert_right('Verb')
        btree.get_left_child().insert_right('Adjective')
        btree.get_right_child().insert_left('Adverb')
        self.assertEqual(btree.get_value(), 'Sentence')
        self.assertEqual(btree.get_left_child().get_value(), 'Noun')
        self.assertEqual(btree.get_right_child().get_value(), 'Verb')
        self.assertEqual(btree.get_right_child().get_left_child().get_value(), 'Adverb')
        self.assertEqual(btree.get_left_child().get_right_child().get_value(), 'Adjective')