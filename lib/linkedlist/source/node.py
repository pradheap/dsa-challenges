# Linked List Node
# A linked list node consist of data that contains a value
# and next field that refers to another Node or None.
# And, it has getter and setter methods.


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next
