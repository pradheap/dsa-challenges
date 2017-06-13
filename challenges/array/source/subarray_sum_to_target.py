

def subarray_sum_no_negatives(arr, target):
    """
    First sub array with sum equals to the target.

    :param arr: List of numbers
    :param target: Target number.
    :return:
    """
    curr_sum = 0
    n = len(arr)
    for i in range(n):
        end = i
        while curr_sum < target and end < n:
            curr_sum += arr[end]
            end += 1
        if curr_sum == target:
            return arr[i:end]
        if curr_sum > target:
            curr_sum = 0

    return None


def subarray_sum_quadratic_runtime(arr, target):
    n = len(arr)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == target:
                return arr[i:j + 1]


def subarray_sum_linear_runtime_and_space(arr, target):
    sum_index = {}
    # In case it starts with first index
    sum_index[0] = -1
    n = len(arr)
    sum_at_i = 0
    # Store cumulative sum in a dict.
    for i in range(n):
        sum_at_i += arr[i]
        diff = sum_at_i - target
        if diff in sum_index:
            return arr[sum_index[diff] + 1: i + 1]
        sum_index[sum_at_i] = i

