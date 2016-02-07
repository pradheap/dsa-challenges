import unittest
from source.lib.node import Node


class TestNode(unittest.TestCase):

    def test_node_data(self):
        value = "node-value"
        changed_value = "changed"
        node = Node(value)
        self.assertEqual(node.get_data(), value)
        node.set_data(changed_value)
        self.assertEqual(node.get_data(), changed_value)

    def test_next_node(self):
        value = "next-node"
        next_node = Node(value)
        node = Node("data", next_node)
        self.assertEqual(node.get_next(), next_node)
        node.set_next(None)
        self.assertEqual(node.get_next(), None)
