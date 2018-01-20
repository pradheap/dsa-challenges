"""
This module contains an implementation of stack data structure
with singly linked list.
"""

from lib.source.linkedlist import Node


class LinkedList:
    """
    A simple linked list implementation
    """
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def delete(self):
        if self.head:
            top_elem = self.head
            self.head = self.head.get_next()
            return top_elem.get_data()
        else:
            return None

    def size(self):
        size = 0
        current = self.head
        while current:
            current = current.get_next()
            size += 1
        return size


class Stack:

    def __init__(self):
        self.ll = LinkedList()

    def push(self, data):
        return self.ll.add(data)

    def pop(self):
        return self.ll.delete()

    def peek(self):
        return self.ll.get_head().get_data()

    def size(self):
        return self.ll.size()