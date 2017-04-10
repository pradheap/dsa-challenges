from challenges.datastructures.tree.source.traversals import in_order


class BSTNode:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def has_children(self):
        return self.has_left_child() or self.has_right_child()

    def get_right_child(self):
        return self.right_child

    def set_value(self, data):
        self.value = data

    def set_right_child(self, subtree):
        self.right_child = subtree

    def set_left_child(self, subtree):
        self.left_child = subtree


class BinarySearchTree:
    def __init__(self, value=None):
        node = None
        if value is not None:
            node = BSTNode(value)
        self.root = node

    def get_root(self):
        return self.root

    def search(self, value, root=None):
        if root is None:
            return None
        if root.get_value() == value:
            return value
        self.search(value, root.get_left_child())
        self.search(value, root.get_right_child())

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._put(self.get_root(), value)

    def _put(self, root, value):
        if root.get_value() < value:
            if root.has_right_child():
                self._put(root.get_right_child(), value)
            else:
                root.set_right_child(BSTNode(value))
        else:
            if root.has_left_child():
                self._put(root.get_left_child(), value)
            else:
                root.set_left_child(BSTNode(value))

    def get(self, value):
        return self._get(self.root, value)

    def _get(self, root, value):
        if root is None:
            return None
        if root.get_value() == value:
            return value
        else:
            if root.get_value() < value:
                return self._get(root.get_right_child(), value)
            else:
                return self._get(root.get_left_child(), value)

    def delete(self, value):
        return self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return None
        if root.get_value() > value:
            root.set_left_child(self._delete(root.get_left_child(), value))
        elif root.get_value() < value:
            root.set_right_child(self._delete(root.get_right_child(), value))
        else:
            if not root.has_left_child():
                temp = root.get_right_child()
                return temp
            elif not root.has_right_child():
                temp = root.get_left_child()
                return temp

            # It has both left and right children
            tmp = self._min_value(root.get_right_child())
            root.set_value(tmp.get_value())
            root.set_right_child(self._delete(root.get_right_child(), tmp.get_value()))
        return root

    @staticmethod
    def _min_value(node):
        current = node
        while current.has_left_child():
            current = current.get_left_child()
        return current


