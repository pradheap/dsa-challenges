

def mirror_tree(root):
    left_tree = root.get_left_child()
    right_tree = root.get_right_child()
    root.set_right_tree(left_tree)
    root.set_left_tree(right_tree)
    if left_tree is not None:
        mirror_tree(left_tree)
    if right_tree is not None:
        mirror_tree(right_tree)
    return root


def is_identical(root1, root2):
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
    # Else if there are children pass them them recursively to the same function.
    if not root.has_left_child() and not root.has_right_child():
        results.append(list(path))
    else:
        recursive_paths(root.get_left_child(), path, results)
        recursive_paths(root.get_right_child(), path, results)

    # After exploring left and right children, pop the current node.
    path.pop()
    return


# BST Problems:

def bst_search(root, value):
    if root is None:
        return False
    if root.get_value() == value:
        return True
    if root.get_value() < value:
        return bst_search(root.get_right_child(), value)
    else:
        return bst_search(root.get_left_child(), value)