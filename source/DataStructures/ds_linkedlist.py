"""
This file contains most of the problems from the linked list problems page.
Pep8 standard naming convention is followed instead of hackerRank's camelcase.
Also, the properties are accessed via getters and setters.
"""


def get_node(head, position):
    """
    Return the data of the Nth Node from the end.
    Takes O(N) extra space
    Input:
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2
    Output:
    6
    3
    :param head: Head of the linked list
    :param position: position starting from tail
    :return: the data at the specific position or None
    """
    values = []
    current = head
    while current is not None:
        values.append(current.get_data())
        current = current.get_next()

    return values[-(position + 1)]



def get_node_improved(head, position):
    """
    Return the data of the Nth Node from the end.
    Takes O(1) extra space

    Input:
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 0
    1 -> 3 -> 5 -> 6 -> NULL, positionFromTail = 2
    Output:
    6
    3
    :param head: Head of the linked list
    :param position: position starting from tail
    :return: the data at the specific position or None
    """
    start_ptr = head
    end_ptr = head

    while position >= 0:
        end_ptr = end_ptr.get_next()
        position -= 1

    while end_ptr is not None:
        start_ptr = start_ptr.get_next()
        end_ptr = end_ptr.get_next()

    return start_ptr.get_data()


def compare_lists(headA, headB):
    """
    Compare two linked lists.

    :param headA: head of the first list
    :param headB: head of the second list
    :return True if both lists are equal, otherwise false.
    """
    currentA = headA
    currentB = headB
    is_equal = True

    while currentA is not None and currentB is not None:
        if currentA.get_data() != currentB.get_data():
            is_equal = False

        currentA = currentA.get_next()
        currentB = currentB.get_next()

    # At this point both pointers should be pointing to None
    if currentA != currentB:
        is_equal = False

    return is_equal


def remove_duplicates(head):
    """
    Delete duplicate nodes from a sorted linked list.

    Sample Input:

    1 -> 1 -> 3 -> 3 -> 5 -> 6 -> NULL
    NULL

    Sample Output:

    1 -> 3 -> 5 -> 6 -> NULL
    NULL


    :param head: head of the linked list.
    :return head of the linked list.
    """
    if head is None:
        return head
    current = head
    while current is not None:
        next_node = current.get_next()
        if next_node and current.get_data() == next_node.get_data():
            current.set_next(next_node.get_next())
            continue
        current = current.get_next()
    return head