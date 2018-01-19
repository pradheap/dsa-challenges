
class Node():
    def __init__(self, key):
        self._key = key
        self._parent = self
        self._rank = 0
    
    def get_parent(self):
        return self._parent
    
    def set_parent(self, parent):
        self._parent = parent
    
    def get_rank(self):
        return self._rank

    def increment_rank(self):
        self._rank += 1
    
    def get_key(self):
        return self._key
    
    def __repr__(self):
        return self.get_key() + ' : ' + self.get_parent().get_key()

class DisjointSet():
    def __init__(self):
        self._nodes = {}

    def make_set(self, x):
        node = Node(x)
        self._nodes[x] = node
    
    def _find_set(self, node):
        if node.get_parent() == node:
            return node
        else:
            node.set_parent(self._find_set(node.get_parent()))
            return node.get_parent()

    def find_set(self, x):
        return self._find_set(self._nodes[x]).get_key()
    
    def merge_set(self, x, y):
        x_rep = self._find_set(self._nodes[x])
        y_rep = self._find_set(self._nodes[y])

        if x_rep == y_rep:
            return

        if x_rep.get_rank() > y_rep.get_rank():
            y_rep.set_parent(x_rep)
        elif x_rep.get_rank() < y_rep.get_rank():
            x_rep.set_parent(y_rep)
        else:
            # arbitrary parent node assignment
            x_rep.set_parent(y_rep)
            y_rep.increment_rank()    
    
    
    


