
class BinaryHeap:
    def __init__(self):
        self.currSize = 0
        self.elements = [0]

    def find_min(self):
        return self.elements[1]

    def _perc_up(self, idx):
        while idx // 2 > 0:
            if self.elements[idx // 2] > self.elements[idx]:
                self.elements[idx // 2], self.elements[idx] = \
                    self.elements[idx], self.elements[idx // 2]
            idx //= 2

    def _perc_down(self, idx):
        while (idx * 2) <= self.currSize:

            smallest_idx = (idx * 2) + 1
            if smallest_idx > self.currSize or self.elements[idx * 2] < self.elements[smallest_idx]:
                smallest_idx = idx * 2

            if self.elements[smallest_idx] < self.elements[idx]:
                self.elements[smallest_idx], self.elements[idx] = \
                    self.elements[idx], self.elements[smallest_idx]
            idx = smallest_idx

    def insert(self, value):
        self.elements.append(value)
        self.currSize += 1
        self._perc_up(self.currSize)


    def delete_min(self):
        ret_value = self.elements[1]
        self.elements[1] = self.elements[self.currSize]
        self.elements.pop()
        self.currSize -= 1
        self._perc_down(1)
        return ret_value

    def build(self, lst):
        mid = len(lst) // 2
        self.currSize = len(lst)
        self.elements = [0] + list(lst)
        while mid > 0:
            self._perc_down(mid)
            mid -= 1

    def get_elements(self):
        return self.elements