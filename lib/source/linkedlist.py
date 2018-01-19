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

class LinkedList:
    def __init__(self):
        self.head = None

    # TODO could improve?
    def add(self, value, pos=0):
        current = self.head

        if pos == 0:
            self.head = Node(value, current)
        else:
            i = 1
            is_added = False
            while current is not None and not is_added:
                if i == pos:
                    new_node = Node(value)
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    is_added = True

                i += 1
                current = current.get_next()

    def remove(self, value):
        current = self.head
        previous = None
        is_removed = False

        while current is not None and not is_removed:
            if current.get_data() == value:
                # The iteration is at the beginning
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                is_removed = True

            previous = current
            current = current.get_next()

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def is_empty(self):
        return self.head is None

    def search(self, value):
        current = self.head
        is_found = False
        while current is not None and not is_found:
            if current.get_data() == value:
                is_found = True
            current = current.get_next()

        return is_found

    def get_head(self):
        return self.head

    def cycle_list(self):
        current = self.head
        next_elem = current.get_next()
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(next_elem)

    def print_data(self):
        current = self.head
        values = ["head"]
        while current is not None:
            values.append(current.get_data())
            current = current.get_next()
        values.append('None')

        print(" --> ".join(map(str, values)))
