

# Kadane Algorithm
def max_sum_subarray_kadane(arr):
    max_sum_so_far = 0
    max_ending_so_far = 0
    elems = []
    res = []
    for elem in arr:
        if elem <= max_ending_so_far + elem:
            elems.append(elem)
            max_ending_so_far += elem
        else:
            elems = [elem]
            max_ending_so_far = elem
        if max_sum_so_far <= max_ending_so_far:
            max_sum_so_far = max_ending_so_far
            res = elems[:]

    # If array contains all -ve numbers.
    if res == [] and max_sum_so_far == 0:
        val = max(arr)
        return [val], val

    return res, max_sum_so_far


def min_sum_subarray_sum(arr):
    min_ending_so_far = 0
    min_sum_so_far = 0
    elems = []
    res = []
    for elem in arr:
        if elem <= min_ending_so_far + elem:
            elems = [elem]
            min_ending_so_far = elem
        else:
            min_ending_so_far += elem
            elems.append(elem)
        if min_sum_so_far >= min_ending_so_far:
            min_sum_so_far = min_ending_so_far
            res = elems[:]

    # If array contains all +ve numbers.
    if res == [] and min_sum_so_far == 0:
        val = min(arr)
        return [val], val

    return res, min_sum_so_far