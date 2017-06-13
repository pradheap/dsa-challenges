import unittest

from challenges.array.source.traversal import linear_traversal, reverse_traversal, zigzag_traversal, \
    reverse_zigzag_traversal


class TestTraversals(unittest.TestCase):
    def test_linear_traversal(self):
        arr = [[1, 2, 3], [4, 6, 8], [10, 13, 16], [24, 20, 16]]
        self.assertEqual([1, 2, 3, 4, 6, 8, 10, 13, 16, 24, 20, 16], linear_traversal(arr))

    def test_reverse_traversal(self):
        arr = [[1, 2, 3], [4, 6, 8], [10, 13, 16], [24, 20, 16]]
        self.assertEqual([16, 20, 24, 16, 13, 10, 8, 6, 4, 3, 2, 1], reverse_traversal(arr))

    def test_zigzag_traversal(self):
        arr = [[1, 2, 3], [4, 6, 8], [10, 13, 16], [24, 20, 16]]
        self.assertEqual([1, 2, 3, 8, 6, 4, 10, 13, 16, 16, 20, 24], zigzag_traversal(arr))

    def test_reverse_zigzag_traversal(self):
        arr = [[1, 2, 3], [4, 6, 8], [10, 13, 16], [24, 20, 16]]
        self.assertEqual([16, 20, 24, 10, 13, 16, 8, 6, 4, 1, 2, 3], reverse_zigzag_traversal(arr))