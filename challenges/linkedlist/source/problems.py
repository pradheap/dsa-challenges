from lib.source.linkedlist import LinkedList

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


def get_nth_node_from_end(head, n):
    """
    Return the data of the Nth Node from the end.
    Takes O(1) extra space.
    Another method in a single loop.

    :param head:
    :param n: position of the node from end.
    :return: the data at the nth node or None
    """
    i = 0
    end_ptr = head
    nth_ptr = head
    while end_ptr and end_ptr.get_next():
        i += 1
        if i >= n:
            nth_ptr = nth_ptr.get_next()
        end_ptr = end_ptr.get_next()

    if i < n:
        return None

    return nth_ptr.get_data()


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
        # If each of the opposite lists are traversed once, and one more time indicates
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


def rotate_right(head, k):
    """
    Given a list, rotate the list to the right by k places, where k is non-negative.

    Input
    1->2->3->4->5->NULL and k = 2,

    Output:
    4->5->1->2->3->NULL.

    :param head: head of a linked list
    :param k: a non-negative integer specifying the number of rotations.
    :return head note of the rotated list.
    """
    current = head
    size = 0
    while current is not None:
        size += 1
        current = current.get_next()

    if k == size or k == 0:
        return head
    else:
        k %= size

    slow = fast = head
    while k:
        fast = fast.get_next()
        k -= 1

    while fast and fast.get_next():
        fast = fast.get_next()
        slow = slow.get_next()

    fast.set_next(head)
    head = slow.get_next()
    slow.set_next(None)

    return head


def rotate_left(head, k):
    """
    Given a list, rotate the list to the left by k places, where k is non-negative.

    Input
    1->2->3->4->5->NULL and k = 2,

    Output:
    3->4->5->1->2->NULL.

    :param head: head of a linked list
    :param k: a non-negative integer specifying the number of rotations.
    :return head note of the rotated list.
    """

    current = head
    size = 0
    while current is not None:
        size += 1
        current = current.get_next()

    if k == size or k == 0:
        return head
    else:
        k %= size

    cut_off = None
    current = head
    idx = 0
    while current and current.get_next():
        idx += 1
        if k == idx:
            cut_off = current
        current = current.get_next()

    current.set_next(head)
    head = cut_off.get_next()
    cut_off.set_next(None)

    return head


def is_palindrome(head):
    """
    Given a list, check whether it's a palindrome.

    Input
    1->2->3->4->5->NULL

    Output:
    False

    Input
    1->2->3->2->1->NULL

    Output:
    True

    :param head: head of a linked list
    :return: a boolean indicating whether the LL is a palindrome.
    """
    stack = []
    slow = fast = head
    palindrome = True

    while fast and fast.get_next() and fast.get_next():
        fast = fast.get_next().get_next()
        stack.append(slow.get_data())
        slow = slow.get_next()

    # If the fast pointer is not None, the list size is odd.
    # so skip the middle element.
    if fast is not None:
        slow = slow.get_next()

    while len(stack) > 0 and slow is not None:
        if slow.get_data() != stack.pop():
            palindrome = False
            break
        slow = slow.get_next()

    return palindrome


def sum_2_numbers(head_a, head_b):
    """
    Given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    Input:
    (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output:
    7 -> 0 -> 8

    Input:
    (8 -> 9) + (2 -> 3)
    Output:
    0 -> 3 -> 1

    :param head_a: the first number
    :param head_b: the second number
    :return: the head of the total.
    """
    curr_a = head_a
    curr_b = head_b

    carry = 0
    new_ll = LinkedList()

    # Including carry in the check, so that the last carry (i.e 1) will be added to the list.
    # If you add a number like this 984 + 93 => 1077, here the 1 because divmod(1, 10) = (0,1)
    while curr_a or curr_b or carry:
        v1 = v2 = 0

        if curr_a:
            v1 = curr_a.get_data()
            curr_a = curr_a.get_next()
        if curr_b:
            v2 = curr_b.get_data()
            curr_b = curr_b.get_next()

        carry, total = divmod(v1 + v2 + carry, 10)
        new_ll.add(total, new_ll.size())

    new_ll.print_data()

    return new_ll.get_head()


def partition_list_even_odd_values(head):
    curr = head
    odd_end_ptr = None
    new_head = None
    prev = None
    i = 0
    while curr is not None:
        if curr.get_data() % 2 != 0:
            if prev:
                prev.set_next(curr.get_next())
            if curr != odd_end_ptr and odd_end_ptr:
                curr.set_next(odd_end_ptr.get_next())
                odd_end_ptr.set_next(curr)
            if odd_end_ptr is None and i > 0:
                new_head = curr
                curr.set_next(prev)
            odd_end_ptr = curr
        prev = curr
        curr = curr.get_next()
        i += 1

    return new_head or head


def partition_list_even_odd_indices(head):
    last_even = head.get_next()
    first_even = last_even
    last_odd = head

    while last_odd.get_next() and last_even.get_next():
        last_odd.set_next(last_even.get_next())
        last_odd = last_odd.get_next()
        last_even.set_next(last_odd.get_next())
        last_even = last_even.get_next()
    last_odd.set_next(first_even)
    return head

