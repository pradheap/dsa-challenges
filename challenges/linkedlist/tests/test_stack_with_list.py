import unittest

from challenges.linkedlist.source.stack_with_list import *


class TestStack(unittest.TestCase):

    def test_stack_methods(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.size(),3)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 20)
        stack.push(60)
        stack.push(90)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 90)
