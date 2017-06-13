# A majority element is any number present more than n/2 times in a list of n elements.
def majority_element(arr):
    majority_elem = arr[0]
    elems_count = 0
    for elem in arr:
        if majority_elem == elem:
            elems_count += 1
        else:
            elems_count -= 1

        if elems_count == 0:
            majority_elem = elem
            elems_count = 1

    # check whether the majority element is really the majority
    majority_count = 0
    total = 0
    for elem in arr:
        if majority_elem == elem:
            majority_count += 1
        total += 1
    if (total / 2) < majority_count:
        return majority_elem
    else:
        return -1