import unittest

from lib.linkedlist.source.linkedlist import LinkedList
from lib.linkedlist.source.node import Node
from challenges.datastructures.linkedlist.source.problems import *


def list_size(head):
    current = head
    size = 0
    while current is not None:
        size += 1
        current = current.get_next()

    return size


class TestLinkedList(unittest.TestCase):

    def test_get_node(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        values = [1, 10, 100, 1000]

        for v in values:
            linked_list.add(v)

        value_1 = get_node(linked_list.head, 2)
        value_2 = get_node_improved(linked_list.head, 2)
        self.assertEqual(value_1, value_2)
        self.assertEqual(100, value_2)

    def test_compare_lists(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()
        values = [1, 10, 100, 1000]

        for v in values:
            linked_list.add(v)
            linked_list1.add(v)

        self.assertTrue(compare_lists(linked_list.get_head(), linked_list1.get_head()))
        linked_list1.remove(10)
        self.assertFalse(compare_lists(linked_list.get_head(), linked_list1.get_head()))

    def test_remove_duplicates(self):
        linked_list = LinkedList()
        values = [900, 600, 500, 500, 400, 400, 300, 200, 170, 90, 27, 1]

        for v in values:
            linked_list.add(v)

        self.assertEqual(linked_list.size(), 12)
        remove_duplicates(linked_list.get_head())
        self.assertEqual(linked_list.size(), 10)

    def test_reverse_list(self):
        linked_list = LinkedList()
        values = [90, 50, 20]

        for v in values:
            linked_list.add(v)

        self.assertEqual(linked_list.size(), 3)
        reversed_list_head = reverse_list(linked_list.get_head())
        self.assertEqual(list_size(reversed_list_head), 3)
        self.assertEqual(reversed_list_head.get_data(), 90)

    def test_merge_lists(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()
        values = [100, 80, 60, 20, 10]
        values1 = [90, 85, 65, 35, 15]

        for v in values:
            linked_list.add(v)
        for v in values1:
            linked_list1.add(v)

        merged_list = merge_lists(linked_list.get_head(), linked_list1.get_head())
        self.assertEqual(list_size(merged_list), 10)

    def test_has_cycle(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()
        values = [20, 50, 60, 80, 90]
        values1 = [20, 50, 60, 34, 43, 45, 54, 65, 67]

        for v in values:
            linked_list.add(v)
        for v in values1:
            linked_list1.add(v)

        linked_list1.cycle_list()
        self.assertEqual(has_cycle(linked_list.get_head()), 0)
        self.assertEqual(has_cycle(linked_list1.get_head()), 1)

    def test_find_merge_node(self):
        # Two linked lists merged together at some node.
        linked_list = LinkedList()
        values = [30, 20, 10]
        values1 = [90, 80, 70, 65, 60, 55, 40, 35, 15, 5, 6, 8]

        for v in values1:
            linked_list.add(v)

        current = linked_list.get_head()
        pos = 5
        while current and current.get_next() is not None:
            if pos == 0:
                connected_node = Node(values[0], current)
                break
            pos -= 1
            current = current.get_next()

        node_2 = Node(values[1], connected_node)
        headB = Node(values[2], node_2)

        self.assertEqual(list_size(headB), 10)
        self.assertEqual(find_merge_node(linked_list.get_head(), headB), 40)

        # Two separate linked lists
        linked_list1 = LinkedList()
        linked_list2 = LinkedList()
        values2 = [20, 50, 60, 80, 90]
        values3 = [20, 50, 60, 34, 43, 45, 54, 65, 67]

        for v in values2:
            linked_list1.add(v)
        for v in values3:
            linked_list2.add(v)

        self.assertEqual(find_merge_node(linked_list1.get_head(), linked_list2.get_head()), None)