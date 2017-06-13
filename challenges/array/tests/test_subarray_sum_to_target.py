import unittest

from challenges.array.source.subarray_sum_to_target import subarray_sum_no_negatives, subarray_sum_quadratic_runtime, \
    subarray_sum_linear_runtime_and_space


class TestTraversals(unittest.TestCase):
    def test_subarray_sum_no_negatives(self):
        self.assertEqual([6, 1], subarray_sum_no_negatives([3, 6, 1, 1], 7))
        self.assertEqual([3, 1, 1, 1, 1], subarray_sum_no_negatives([3, 1, 1, 1, 1], 7))
        self.assertEqual([5], subarray_sum_no_negatives([3, 3, 5, 1, 1, 1], 5))
        self.assertEqual([1, 2, 3, 1], subarray_sum_no_negatives([4, 9, 2, 1, 2, 3, 1, 1, 1], 7))
        self.assertEqual([3,4], subarray_sum_no_negatives([1, 2, 3, 4, 9], 7))
        self.assertIsNone(subarray_sum_no_negatives([1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1], 16))
        self.assertEqual([3, 4], subarray_sum_no_negatives([3, 4, 7, 1], 7))
        self.assertIsNone(subarray_sum_no_negatives([3, 4, 7, 1], 5))
        self.assertEqual([7], subarray_sum_no_negatives([3, 5, 7, 1], 7))

    def test_subarray_sum_quadratic_runtime(self):
        self.assertEqual([2, 3], subarray_sum_quadratic_runtime([1, 2, 3], 5))
        self.assertEqual([-12, 14, 13], subarray_sum_quadratic_runtime([11, 21, -12, 14, 13], 15))
        self.assertEqual([4], subarray_sum_quadratic_runtime([1, 21, 2, -12, 1, 1, 4, 12], 4))
        self.assertEqual([1, 21, 2, -12], subarray_sum_quadratic_runtime([1, 21, 2, -12, 1, 1, 4], 12))
        self.assertEqual([7], subarray_sum_quadratic_runtime([1, 21, 2, -12, 1, 1, 7], 7))
        self.assertEqual([-2, 11], subarray_sum_quadratic_runtime([-2, 11, 2, -12, 1, 1, 7], 9))
        self.assertEqual([-2, 11, 2, -11], subarray_sum_linear_runtime_and_space([-2, 11, 2, -11, 1, 1, 7], 0))
        self.assertEqual([4, -4], subarray_sum_linear_runtime_and_space([-2, 11, 4, -4, 1, 1, 7], 0))
        self.assertIsNone(subarray_sum_quadratic_runtime([-2, 11, 2, -12, 1, 1, 7], 19))
        self.assertIsNone(subarray_sum_quadratic_runtime([-2, 11, 2, -12, 1, 1, 7], 29))

    def test_subarray_sum_linear_runtime_and_space(self):
        self.assertEqual([2, 3], subarray_sum_linear_runtime_and_space([1, 2, 3], 5))
        self.assertEqual([-12, 14, 13], subarray_sum_linear_runtime_and_space([11, 21, -12, 14, 13], 15))
        self.assertEqual([4], subarray_sum_linear_runtime_and_space([1, 21, 2, -12, 1, 1, 4, 12], 4))
        self.assertEqual([1, 21, 2, -12], subarray_sum_linear_runtime_and_space([1, 21, 2, -12, 1, 1, 4], 12))
        self.assertEqual([7], subarray_sum_linear_runtime_and_space([1, 21, 2, -12, 1, 1, 7], 7))
        self.assertEqual([-2, 11], subarray_sum_linear_runtime_and_space([-2, 11, 2, -12, 1, 1, 7], 9))
        self.assertEqual([-2, 11, 2, -11], subarray_sum_linear_runtime_and_space([-2, 11, 2, -11, 1, 1, 7], 0))
        self.assertEqual([4, -4], subarray_sum_linear_runtime_and_space([-2, 11, 4, -4, 1, 1, 7], 0))
        self.assertIsNone(subarray_sum_linear_runtime_and_space([-2, 11, 2, -12, 1, 1, 7], 19))
        self.assertIsNone(subarray_sum_linear_runtime_and_space([-2, 11, 2, -12, 1, 1, 7], 29))