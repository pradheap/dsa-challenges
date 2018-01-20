

def mirror_tree(root):
    """
    Mirror a given tree.

    Input:
          3
       1     2
     4   5     6
    Output:
            3
        2       1
      6      5     4
    :param root: root node of the binary tree.
    :return: the root of the mirrored tree.
    """
    left_tree = root.get_left_child()
    right_tree = root.get_right_child()
    root.set_right_tree(left_tree)
    root.set_left_tree(right_tree)
    if left_tree is not None:
        mirror_tree(left_tree)
    if right_tree is not None:
        mirror_tree(right_tree)
    return root


def get_height(root):
    """
    Given a root of the tree, find it's max height.
    The height of the tree is the max height of either one of its subtrees.

    Input:
    1

    Output:
    0

    Input:
         2
       1   3

    Output:
    1

    Input:
          2
        1
     4    3

    Output:
    2

    :param root: root of the binary tree
    :return: the height of the binary tree
    """
    if root is None:
        return -1

    left_height = get_height(root.get_left_child())
    right_height = get_height(root.get_right_child())
    return 1 + max(left_height, right_height)


def is_identical(root1, root2):
    """
    Given root nodes of two trees, check whether they're identical.

    :param root1: root node of a tree
    :param root2: root node of another tree
    :return: a boolean to indicate whether they're identical.
    """
    if root1 is None and root2 is not None:
        return False
    if root2 is None and root1 is not None:
        return False
    if root1 is None and root2 is None:
        return True
    is_equal = root1.get_value() == root2.get_value()
    is_equal = is_equal and is_identical(root1.get_left_child(), root2.get_left_child())
    is_equal = is_equal and is_identical(root1.get_right_child(), root2.get_right_child())
    return is_equal


def all_paths(root):
    """
    Return all the paths of a binary tree from root node to leaf nodes.

    Input:
               3
         6           7
      4     5     8     9
    1   7    2             10
    Output:
    [[3,6,4,1], [3,6,4,7], [3,6,5,2], [3,7,8], [3,7,9,10]]

    :param root: root node of a binary tree.
    :return: A list of the paths from root node to leaf node.
    """
    path, results = [], []
    recursive_paths(root, path, results)
    return results


def recursive_paths(root, path, results):
    # If the root is none, return
    if root is None:
        return

    # If the root is not none, add the value to the path
    path.append(root.get_value())

    # If there is no left and right child, add the path to the results
    # Else if there are children pass them recursively to the same function.
    if not root.has_left_child() and not root.has_right_child():
        results.append(list(path))
    else:
        recursive_paths(root.get_left_child(), path, results)
        recursive_paths(root.get_right_child(), path, results)

    # After exploring left and right children, pop the current node.
    path.pop()
    return


def common_ancestor(root, value1, value2):
    """
    Lowest Common Ancestor of a pair of values.

    :param root: root of the binary tree
    :param value1: The first value
    :param value2: The second value
    :return: the lowest common ancestor node's value
    """
    if root is None:
        return None
    if root.get_value() == value1 or root.get_value() == value2:
        return root.get_value()

    left_parent = common_ancestor(root.get_left_child(), value1, value2)
    right_parent = common_ancestor(root.get_right_child(), value1, value2)

    if left_parent is not None and right_parent is not None:
        return root.get_value()

    return left_parent or right_parent


def is_height_balanced(root):
    """
    Given a tree, find whether it's height balanced.
    Height balanced is when the difference between left and right subtree's height is not more than 1.

    :param root: a root of a binary tree,
    :return: a boolean to indicate the balanced-ness.
    """
    if root is None:
        return True

    left_height = get_height(root.get_left_child())
    right_height = get_height(root.get_right_child())

    if abs(left_height - right_height) <= 1 and is_height_balanced(root.get_left_child()) and \
            is_height_balanced(root.get_right_child()):
        return True

    return False


# BST Problems:

def bst_search(root, value):
    """
    Search for the value in a BST.

    :param root: root of a binary tree.
    :param value: value to be searched for.
    :return: a boolean value that indicates whether the value is present or not.
    """
    if root is None:
        return False
    if root.get_value() == value:
        return True
    if root.get_value() < value:
        return bst_search(root.get_right_child(), value)
    else:
        return bst_search(root.get_left_child(), value)