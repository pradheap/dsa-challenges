import unittest

from challenges.sorting.source.index import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        unsorted_list = [108, 209, 2080, 4060, 3040, 5000, 6000, 3456, 96, 45, 32, 65, 4, 51, 89]
        sorted_list = [4, 32, 45, 51, 65, 89, 96, 108, 209, 2080, 3040, 3456, 4060, 5000, 6000]
        result = bubble_sort(unsorted_list)
        self.assertListEqual(result, sorted_list)


# print(sort([random.randint(10, 1000001) for _ in xrange(100)]))
#
# if __name__ == '__main__':
#     import timeit
#
#     print(timeit.timeit("sort([random.randint(10,100000) for _ in xrange(1000)])",
#                         setup="import random; from __main__ import sort", number=1))