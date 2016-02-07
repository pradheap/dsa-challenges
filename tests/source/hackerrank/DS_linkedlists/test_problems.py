import unittest

from source.lib.linkedlist import LinkedList
from source.hackerrank.DS_linkedlists import problems


class TestNode(unittest.TestCase):

    def test_get_node(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
        linked_list.print()
        value = problems.get_node(linked_list.head, 2)
        self.assertEqual(100, value)
