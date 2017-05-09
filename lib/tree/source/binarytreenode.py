class BinaryTreeNode:
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

    def set_value(self, data):
        self.value = data

    def set_right_tree(self, subtree):
        self.right_child = subtree

    def set_left_tree(self, subtree):
        self.left_child = subtree

    def insert_left(self, data):
        new_node = BinaryTreeNode(data)
        if self.left_child is None:
            self.left_child = new_node
        else:
            left_tree = self.left_child
            self.left_child = new_node
            new_node.left_child = left_tree

    def insert_right(self, data):
        new_node = BinaryTreeNode(data)
        if self.right_child is None:
            self.right_child = new_node
        else:
            right_tree = self.right_child
            self.right_child = new_node
            new_node.right_child = right_tree