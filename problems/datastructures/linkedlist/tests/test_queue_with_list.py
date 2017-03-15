import unittest

from problems.datastructures.linkedlist.source.queue_with_list import *


class TestStack(unittest.TestCase):

    def test_queue_methods(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.size(),3)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.peek(), 2)
        queue.enqueue(60)
        queue.enqueue(80)
        self.assertEqual(queue.size(), 4)
        self.assertEqual(queue.peek(), 2)
