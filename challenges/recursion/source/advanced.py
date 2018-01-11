def group_sum(start, arr, target):
    if start >= len(arr):
        return target == 0
    return group_sum(start + 1, arr, target - arr[start]) or group_sum(start + 1, arr, target)

def group_sum6(start, arr, target):
    if start >= len(arr):
        return target == 0
    if arr[start] == 6:
        return group_sum6(start + 1, arr, target - arr[start])
    return group_sum6(start + 1, arr, target - arr[start]) or group_sum6(start + 1, arr, target)

def group_no_adj(start, arr, target):
    if start >= len(arr):
        return target == 0
    return group_no_adj(start + 2, arr, target - arr[start]) or group_no_adj(start + 1, arr, target)
 
def group_sum_5(start, arr, target):
    if start >= len(arr):
        return target == 0
    if arr[start] % 5 == 0:
        if start + 1 < len(arr) and arr[start + 1] == 1:
            return group_sum_5(start + 2, arr, target)
        return group_sum_5(start + 1, arr, target - arr[start])
    return group_sum_5(start + 1, arr, target - arr[start]) or group_sum_5(start + 1, arr, target)

def group_sum_clump(start, arr, target):
    if start >= len(arr):
        return target == 0
    if start + 1 < len(arr) and arr[start] == arr[start + 1]:
        return group_sum_clump(start + 2, arr, target - (2 * arr[start]))
    if arr[start - 1] == arr[start]:
        return group_sum_clump(start + 1, arr, target - arr[start])
    return group_sum_clump(start + 1, arr, target - arr[start]) or group_sum_clump(start + 1, arr, target)

def split_array(arr):
    def recursive_split_array(start, arr, sum1, sum2):
        if start >= len(arr):
            return sum1 == sum2
        return recursive_split_array(start + 1, arr, sum1 + arr[start], sum2) or recursive_split_array(start + 1, arr, sum1, sum2 + arr[start])
    return recursive_split_array(0, arr, 0, 0)

def split_odd_10(arr):
    def recursive_split_odd_10(start, arr, sum1, sum2):
        if start >= len(arr):
            return sum1 % 10 == 0 and sum2 % 2 != 0
        return recursive_split_odd_10(start + 1, arr, sum1 + arr[start], sum2) or recursive_split_odd_10(start + 1, arr, sum1, arr[start] + sum2)

    return recursive_split_odd_10(0, arr, 0, 0)

def split_53(arr):
    def recursive_split_53(start, arr, sum1, sum2):
        if start >= len(arr):
            return sum1 == sum2
        if arr[start] % 5 == 0:
            return recursive_split_53(start + 1, arr, sum1 + arr[start], sum2)
        if arr[start] % 3 == 0:
            return recursive_split_53(start + 1, arr, sum1, sum2 + arr[start])
        return recursive_split_53(start + 1, arr, sum1 + arr[start], sum2) or recursive_split_53(start + 1, arr, sum1, arr[start] + sum2)

    return recursive_split_53(0, arr, 0, 0)
