import unittest

from source.DataStructures.ds_linkedlist import *
from source.lib.linkedlist import LinkedList


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
