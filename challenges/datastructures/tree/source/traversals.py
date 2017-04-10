from challenges.datastructures.linkedlist.source.queue_with_list import Queue


def pre_order(root):
    result = []
    if root is None:
        return result

    result.append(root.get_value())
    result.extend(pre_order(root.get_left_child()))
    result.extend(pre_order(root.get_right_child()))

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
        return -1

    left_height = get_height(root.get_left_child())
    right_height = get_height(root.get_right_child())
    return 1 + max(left_height, right_height)


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


def iterative_pre_order(root):
    stack = []
    result = []

    if root is not None:
        stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            result.append(node.get_value())
            stack.append(node.get_right_child())
            stack.append(node.get_left_child())
    return result


def iterative_in_order(root):
    stack = []
    result = []

    current = root
    stack.append(current)
    while len(stack) > 0:
        if current is not None and current.has_left_child():
            current = current.get_left_child()
            stack.append(current)
        else:
            node = stack.pop()
            result.append(node.get_value())
            if node.has_right_child():
                stack.append(node.get_right_child())
                current = node.get_right_child()
    return result


def iterative_post_order(root):
    stack = []
    result = []

    current = root
    while current is not None or len(stack) > 0:

        if current is not None:
            stack.append(current)
            current = current.get_left_child()
        else:
            tmp = stack[len(stack) - 1].get_right_child()
            if tmp is None:
                tmp = stack.pop()
                result.append(tmp.get_value())
                while len(stack) > 0 and tmp == stack[len(stack) - 1].get_right_child():
                    tmp = stack.pop()
                    result.append(tmp.get_value())
            else:
                current = tmp

    return result
