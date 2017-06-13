import unittest

from challenges.array.source.majority_element import majority_element


class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        self.assertEqual(2, majority_element([1, 2, 2]))
        self.assertEqual(1, majority_element([1, 2, 2, 1, 1]))
        self.assertEqual(-1, majority_element([1, 2, 2, 1]))
        self.assertEqual(1, majority_element([1, 1]))
        self.assertEqual(-1, majority_element([1, 2, 3]))
