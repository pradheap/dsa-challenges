## ds_linkedlist

This module contains soultions for most of the linked list problems found
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

    has_cycle(head)
        Cycle detection in a linked list.
        0 - if there was no cycle.
        1 - if there was a cycle.

        :param head: head of a linked list
        :return return whether a cycle was detected.

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