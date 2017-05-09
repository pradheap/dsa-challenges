## ds_linkedlist

This module contains solutions for most of the linked list problems found
across the WWW ranging from sites such as hackerrank, geekforgeeks and other random sites.
Pep8 standard naming convention is followed.
The properties are accessed or mutated via getters and setters.

FUNCTIONS

    compare_lists(a_head, b_head)
        Compare two linked lists.

        :param a_head: head of the first list
        :param b_head: head of the second list
        :return True if both lists are equal, otherwise false.

    find_merge_node(a_head, b_head)
        Given pointers to the head nodes of linked lists that merge together at some node,
        find the Node where the two lists merge.

        Input:
        14-->28-->93
                    \
                    43-->53-->None
                   /
            10-->20

        Output:
        43


        :param a_head: head of a linked list
        :param b_head: head of another linked list
        :return node where lists merge or None if lists don't merge together.

    get_node(head, position)
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

    get_node_improved(head, position)
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

    get_nth_node_from_end(head, n)
        Return the data of the Nth Node from the end.
        Takes O(1) extra space.
        Another method in a single loop.

        :param head:
        :param n: position of the node from end.
        :return: the data at the nth node or None

    has_cycle(head)
        Cycle detection in a linked list.
        0 - if there was no cycle.
        1 - if there was a cycle.

        :param head: head of a linked list
        :return return whether a cycle was detected.

    is_palindrome(head)
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

    merge_lists(a_head, b_head)
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

    remove_duplicates(head)
        Delete duplicate nodes from a sorted linked list.

        Sample Input:

        1 -> 1 -> 3 -> 3 -> 5 -> 6 -> NULL
        NULL

        Sample Output:

        1 -> 3 -> 5 -> 6 -> NULL
        NULL

        :param head: head of the linked list.
        :return head of the linked list.

    reverse_list(head)
        Reverse a linked list.

        Sample Input:

        1 -> 4 -> 3 -> NULL
        NULL

        Sample Output:

        3 -> 4 -> 1 -> NULL
        NULL

        :param head: head of the linked list.
        :return head of the linked list.

    rotate_left(head, k)
        Given a list, rotate the list to the left by k places, where k is non-negative.

        Input
        1->2->3->4->5->NULL and k = 2,

        Output:
        3->4->5->1->2->NULL.

        :param head: head of a linked list
        :param k: a non-negative integer specifying the number of rotations.
        :return head note of the rotated list.

    rotate_right(head, k)
        Given a list, rotate the list to the right by k places, where k is non-negative.

        Input
        1->2->3->4->5->NULL and k = 2,

        Output:
        4->5->1->2->3->NULL.

        :param head: head of a linked list
        :param k: a non-negative integer specifying the number of rotations.
        :return head note of the rotated list.

    sum_2_numbers(head_a, head_b)
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
