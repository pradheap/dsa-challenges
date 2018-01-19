import unittest

from lib.source.linkedlist import LinkedList, Node


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

    def test_list_add(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
        self.assertEqual(linked_list.size(), len(values))

    def test_list_search(self):
        linked_list = LinkedList()
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
        self.assertTrue(linked_list.search(10))
        self.assertFalse(linked_list.search(2))

    def test_list_remove(self):
        linked_list = LinkedList()
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
        linked_list.remove(10)
        self.assertEqual(linked_list.size(), len(values) - 1)
        linked_list.remove(2)
        self.assertEqual(linked_list.size(), len(values) - 1)
        linked_list.remove(1000)
        self.assertEqual(linked_list.size(), len(values) - 2)
