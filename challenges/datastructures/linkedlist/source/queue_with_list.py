"""
This module contains an implementation of queue data structure
with singly linked list.
"""

from lib.linkedlist.source.node import Node


class LinkedList:
    """
    A simple linked list implementation
    """
    def __init__(self):
        """
        Initializing 'tail' instance variable along with 'head'
        to avoid O(N) to traverse to the end of LL to insert an
        element for enqueue operation.
        """
        self.head = None
        self.tail = None

    def get_head(self):
        """

        :return: head of the linked list.
        """
        return self.head

    def get_tail(self):
        """

        :return: tail of the linked list.
        """
        return self.tail

    def add_to_tail(self, data):
        """
        Add a new node with the input data to the end.

        :param data: data for creating new node.
        :return:
        """
        new_node = Node(data)
        if self.tail is not None:
            # if the tail refers to a node, then make the new node as the next node of the
            # existing tail node and the tail refers to the new node.
            self.tail.set_next(new_node)
            self.tail = self.tail.get_next()
        else:
            # Else head and tail refers to the same node.
            self.head = new_node
            self.tail = new_node

    def delete(self):
        """
        Delete the foremost element from the linked list.

        :return:
        """
        if self.head:
            top_elem = self.head
            self.head = self.head.get_next()
            if self.head is None:
                self.tail = None
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


class Queue:

    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, data):
        return self.ll.add_to_tail(data)

    def dequeue(self):
        return self.ll.delete()

    def peek(self):
        return self.ll.get_head().get_data()

    def size(self):
        return self.ll.size()