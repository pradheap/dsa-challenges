"""
This module contains solutions for most of the linked list problems found
across the WWW ranging from sites such as hackerrank, geekforgeeks and other random sites.
Pep8 standard naming convention is followed.
The properties are accessed or mutated via getters and setters.
"""


def get_node(head, position):
    """
    Return the data of the Nth Node from the end.
    Takes O(N) extra space.

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
    Takes O(1) extra space.

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


def compare_lists(a_head, b_head):
    """
    Compare two linked lists.

    :param a_head: head of the first list
    :param b_head: head of the second list
    :return True if both lists are equal, otherwise false.
    """
    a_current = a_head
    b_current = b_head
    is_equal = True

    while a_current is not None and b_current is not None:
        if a_current.get_data() != b_current.get_data():
            is_equal = False

        a_current = a_current.get_next()
        b_current = b_current.get_next()

    # At this point both pointers should be pointing to None
    if a_current != b_current:
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


def reverse_list(head):
    """
    Reverse a linked list.

    Sample Input:

    1 -> 4 -> 3 -> NULL
    NULL

    Sample Output:

    3 -> 4 -> 1 -> NULL
    NULL

    :param head: head of the linked list.
    :return head of the linked list.
    """
    current = head
    prev = None

    while current is not None:
        next_node = current.get_next()
        current.set_next(prev)

        # Iterate
        prev = current
        current = next_node

    # At last, the next points to None and prev to last node.
    head = prev
    return head


def merge_lists(a_head, b_head):
    """
    Merge two linked lists that are sorted.

    Sample Input:

    3 -> 4 -> 6 -> 8 -> NULL
    2 -> 5 -> 7 -> NULL

    13 -> NULL
    11 -> NULL

    NULL
    2-> 3 -> NULL

    Sample Output:

    2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
    11 -> 13 -> NULL
    2 -> 3 -> NULL

    :param a_head: head of the list A
    :param b_head: head of the list B
    :return: head of the combined list

    """

    if a_head is None:
        return b_head
    elif b_head is None:
        return a_head

    # Choose the smaller data as the current pointer another as other pointer.
    if a_head.get_data() < b_head.get_data():
        return_head = a_head
        other = b_head
    else:
        return_head = b_head
        other = a_head

    current = return_head

    while current is not None:
        if current.get_data() < other.get_data() and current.get_next() and \
                        current.get_next().get_data() > other.get_data():
            tmp = other
            other = current.get_next()
            current.set_next(tmp)

        if current.get_next() is None:
            current.set_next(other)
            break

        current = current.get_next()

    return return_head


def has_cycle(head):
    """
    Cycle detection in a linked list.
    0 - if there was no cycle.
    1 - if there was a cycle.

    :param head: head of a linked list
    :return return whether a cycle was detected.
    """
    slow_ptr = head
    fast_ptr = head
    is_cycle = 0
    # Based on floyds cycle detection algorithm.
    while fast_ptr and fast_ptr.get_next():
        slow_ptr = slow_ptr.get_next()
        # fast_ptr.get_next().get_next() could be None and the end of list.
        fast_ptr = fast_ptr.get_next().get_next()
        if slow_ptr == fast_ptr:
            is_cycle = 1
            break

    return is_cycle


def find_merge_node(a_head, b_head):
    """
    Given pointers to the head nodes of linked lists that merge together at some node,
    find the Node where the two lists merge.

    Input:
    14-->28-->93
                \\
                43-->53-->None
               /
        10-->20

    Output:
    43

    :param a_head: head of a linked list
    :param b_head: head of another linked list
    :return node where lists merge or None if lists don't merge together.
    """
    a_current = a_head
    b_current = b_head
    # To keep track of the iteration on the opposite lists.
    iteration_count = 0

    # Each pointer traverses a list once and in the end, it starts traversing the opposite list.
    # At some node, both pointer meets and that's the merge node.
    while not a_current == b_current:
        # If each of the opposite lists are traversed once, and one more tiem indicates
        # that the the lists are separate and doesn't contain the merge node.
        if iteration_count > 2:
            return None

        if a_current.get_next() is None:
            iteration_count += 1
            a_current = b_head
        else:
            a_current = a_current.get_next()

        if b_current.get_next() is None:
            iteration_count += 1
            b_current = a_head
        else:
            b_current = b_current.get_next()

    return a_current.get_data()