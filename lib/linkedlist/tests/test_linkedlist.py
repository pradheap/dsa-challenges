import unittest

from lib.linkedlist.source.linkedlist import LinkedList


class TestNode(unittest.TestCase):
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
