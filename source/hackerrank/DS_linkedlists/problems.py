"""
This file contains most of the problems from the linked list problems page.
Pep8 standard naming convention is followed instead of hackerRank's camelcase.
Also, the properties are accessed via getters and setters.
"""
from source.lib.linkedlist import LinkedList


# Return the data of the Nth Node from the end.
def get_node(head, position):
    """
    Input:
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2
    Output:
    6
    3
    :param head: Head of the linked list
    :param position: Position from tail
    :return: respective data or None
    """
    values = []
    current = head
    while current is not None:
        values.append(current.get_data())
        current = current.get_next()

    return values[-(position + 1)]