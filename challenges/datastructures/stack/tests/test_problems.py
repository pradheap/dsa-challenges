import unittest

from challenges.datastructures.stack.source.problems import *


class TestStackProblems(unittest.TestCase):

    def test_stack_api(self):
        stack = Stack()
        self.assertEqual(0, stack.size())
        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        stack.push(55)
        stack.push(65)
        self.assertEqual(2, stack.size())
        self.assertFalse(stack.is_empty())
        self.assertEqual(65, stack.peek())
        self.assertEqual(65, stack.pop())
        self.assertEqual(55, stack.pop())
        self.assertEqual(0, stack.size())
        self.assertTrue(stack.is_empty())

    def test_balanced_parantheses(self):
        self.assertTrue(balanced_parentheses('{}'))
        self.assertTrue(balanced_parentheses('{[]}'))
        self.assertFalse(balanced_parentheses('{{[]}'))
        self.assertFalse(balanced_parentheses('{{[]}}]'))
        self.assertFalse(balanced_parentheses('{({[]}}]'))

    def test_convert_decimal_to_any_base(self):
        self.assertEqual(bin(0), convert_decimal_to_any_base(0,2))
        self.assertEqual(bin(1), convert_decimal_to_any_base(1,2))
        self.assertEqual(bin(2), convert_decimal_to_any_base(2,2))
        self.assertEqual(bin(3), convert_decimal_to_any_base(3,2))
        self.assertEqual(bin(4), convert_decimal_to_any_base(4,2))
        self.assertEqual(bin(40), convert_decimal_to_any_base(40,2))
        self.assertEqual(bin(14), convert_decimal_to_any_base(14,2))
        self.assertEqual(bin(101), convert_decimal_to_any_base(101,2))
        self.assertEqual(bin(10001), convert_decimal_to_any_base(10001,2))
        self.assertEqual(hex(10001), convert_decimal_to_any_base(10001,16))
        self.assertEqual(hex(1), convert_decimal_to_any_base(1,16))
        self.assertEqual(hex(0), convert_decimal_to_any_base(0,16))
        self.assertEqual(hex(16), convert_decimal_to_any_base(16,16))
        self.assertEqual(hex(17), convert_decimal_to_any_base(17,16))
        self.assertEqual(oct(8), convert_decimal_to_any_base(8,8))
        self.assertEqual(oct(7), convert_decimal_to_any_base(7,8))
        self.assertEqual(oct(9), convert_decimal_to_any_base(9,8))
        self.assertEqual(oct(0), convert_decimal_to_any_base(0,8))


