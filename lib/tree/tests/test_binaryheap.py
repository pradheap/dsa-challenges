import unittest

from lib.tree.source.binaryheap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def test_build_heap(self):
        lst = [19, 15, 12, 20, 9, 1, 4, 8, 11, 6, 5, 7, 2, 3, 10, 14]
        heap = BinaryHeap()
        heap.build(lst)
        self.assertListEqual([0, 1, 5, 2, 8, 6, 7, 3, 14, 11, 15, 9, 19, 12, 4, 10, 20], heap.get_elements())
        self.assertEqual(1, heap.find_min())
        self.assertEqual(1, heap.delete_min())
        self.assertEqual(2, heap.delete_min())
        self.assertEqual(3, heap.delete_min())
        self.assertListEqual([0, 4, 5, 7, 8, 6, 12, 10, 14, 11, 15, 9, 19, 20], heap.get_elements())
        heap.insert(2)
        heap.insert(1)
        self.assertListEqual([0, 1, 5, 2, 8, 6, 12, 4, 14, 11, 15, 9, 19, 20, 10, 7], heap.get_elements())
        self.assertEqual(1, heap.find_min())
        self.assertEqual(1, heap.delete_min())
        self.assertEqual(2, heap.delete_min())
        self.assertEqual(4, heap.delete_min())
        self.assertListEqual([0, 5, 6, 7, 8, 9, 12, 10, 14, 11, 15, 20, 19], heap.get_elements())
