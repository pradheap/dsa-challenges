from problems.datastructures.linkedlist.source.queue_with_list import Queue

def pre_order(root):
    result = []
    if root is None:
        return result

    result.append(root.get_value())
    result = result + pre_order(root.get_left_child())
    result = result + pre_order(root.get_right_child())

    return result


def post_order(root):
    result = []
    if root is None:
        return result

    result = result + post_order(root.get_left_child())
    result = result + post_order(root.get_right_child())
    result.append(root.get_value())

    return result


def in_order(root):
    result = []
    if root is None:
        return result

    result = result + in_order(root.get_left_child())
    result.append(root.get_value())
    result = result + in_order(root.get_right_child())

    return result


def get_height(root):
    if root is None:
        return 0
    else:
        left_height = 1 + get_height(root.get_left_child())
        right_height = 1 + get_height(root.get_right_child())
        return max(left_height, right_height)


def level_order(root):
    q = Queue()
    result = []
    if root is None:
        return result

    q.enqueue(root)
    while q.size() > 0:
        root = q.dequeue()
        result.append(root.get_value())
        if root.get_left_child() is not None:
            q.enqueue(root.get_left_child())
        if root.get_right_child() is not None:
            q.enqueue(root.get_right_child())

    return result