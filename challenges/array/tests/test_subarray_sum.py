import unittest

from challenges.array.source.subarray_sum import max_sum_subarray_kadane, min_sum_subarray_sum


class TestSubArraySum(unittest.TestCase):
    def test_max_sum_subarray_kadane(self):
        self.assertEqual(([4, 3, 5], 12), max_sum_subarray_kadane([4, 3, 5, -2, 1, -5]))
        self.assertEqual(([4, -2, 5], 7), max_sum_subarray_kadane([4, -2, 5, -2, 1, -1]))
        self.assertEqual(([5, -2, 3], 6), max_sum_subarray_kadane([1, -4, -3, 5, -2, 3, -5]))
        self.assertEqual(([5, -2, 4, 5], 12), max_sum_subarray_kadane([11, -9, -3, 5, -2, 4, 5]))
        self.assertEqual(([-2], -2), max_sum_subarray_kadane([-11, -9, -3, -5, -2, -4, -5]))

    def test_min_sum_subarray_sum(self):
        self.assertEqual(([-2, 1, -5], -6), min_sum_subarray_sum([4, 3, 5, -2, 1, -5]))
        self.assertEqual(([-2, 1, -1], -2), min_sum_subarray_sum([4, -2, 5, -2, 1, -1]))
        self.assertEqual(([-4, -3], -7), min_sum_subarray_sum([1, -4, -3, 5, -2, 3, -5]))
        self.assertEqual(([-9, -3, 5, 2, -4, -5], -14), min_sum_subarray_sum([11, -9, -3, 5, 2, -4, -5]))
        self.assertEqual(([2], 2), min_sum_subarray_sum([11, 9, 3, 5, 2, 4, 5]))