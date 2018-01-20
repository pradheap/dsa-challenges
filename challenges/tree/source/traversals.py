from challenges.linkedlist.source.queue_with_list import Queue


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


def reverse_level_order(root):
    q = Queue()
    s = []
    result = []
    if root is None:
        return result

    q.enqueue(root)
    while q.size() > 0:
        node = q.dequeue()
        if node.has_right_child():
            q.enqueue(node.get_right_child())
        if node.has_left_child():
            q.enqueue(node.get_left_child())
        s.append(node.get_value())

    while len(s) > 0:
        result.append(s.pop())

    return result


def zig_zag_level_order(root):
    s1 = []
    s2 = []
    result = []

    if root is None:
        return result
    s1.append(root)
    while len(s1) or len(s2) > 0:
        while len(s2) > 0:
            curr = s2.pop()
            if curr.has_right_child():
                s1.append(curr.get_right_child())
            if curr.has_left_child():
                s1.append(curr.get_left_child())
            result.append(curr.get_value())
        while len(s1) > 0:
            curr = s1.pop()
            if curr.has_left_child():
                s2.append(curr.get_left_child())
            if curr.has_right_child():
                s2.append(curr.get_right_child())
            result.append(curr.get_value())
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


def iterative_post_order_two_stacks(root):
    s1 = []
    s2 = []
    result = []
    s1.append(root)
    while len(s1) > 0:
        curr = s1.pop()
        s2.append(curr.get_value())
        if curr.has_left_child():
            s1.append(curr.get_left_child())
        if curr.has_right_child():
            s1.append(curr.get_right_child())

    while len(s2) > 0:
        result.append(s2.pop())

    return result
