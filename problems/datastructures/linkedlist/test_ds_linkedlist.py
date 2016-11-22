import unittest

from lib.linkedlist.source.linkedlist import LinkedList
from problems.datastructures.linkedlist.ds_linkedlist import *


def list_size(head):
    current = head
    size = 0
    while current is not None:
        size += 1
        current = current.get_next()

    return size


class TestNode(unittest.TestCase):

    def test_get_node(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
        linked_list.print_data()
        value_1 = get_node(linked_list.head, 2)
        value_2 = get_node_improved(linked_list.head, 2)
        self.assertEqual(value_1, value_2)
        self.assertEqual(100, value_2)

    def test_compare_lists(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertTrue(linked_list1.is_empty())
        values = [1, 10, 100, 1000]
        for v in values:
            linked_list.add(v)
            linked_list1.add(v)
        linked_list.print_data()
        linked_list1.print_data()
        self.assertTrue(compare_lists(linked_list.get_head(), linked_list1.get_head()))
        linked_list1.remove(10)
        self.assertFalse(compare_lists(linked_list.get_head(), linked_list1.get_head()))

    def test_remove_duplicates(self):
        linked_list = LinkedList()
        values = [900, 600, 500, 500, 400, 400, 300, 200, 170, 90, 27, 1]
        for v in values:
            linked_list.add(v)
        linked_list.print_data()
        self.assertEqual(linked_list.size(), 12)
        remove_duplicates(linked_list.get_head())
        linked_list.print_data()
        self.assertEqual(linked_list.size(), 10)

    def test_reverse_list(self):
        linked_list = LinkedList()
        values = [90, 50, 20]
        for v in values:
            linked_list.add(v)
        linked_list.print_data()
        self.assertEqual(linked_list.size(), 3)
        reversed_list_head = reverse_list(linked_list.get_head())
        self.assertEqual(list_size(reversed_list_head), 3)
        self.assertEqual(reversed_list_head.get_data(), 90)
