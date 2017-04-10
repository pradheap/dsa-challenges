def bubble_sort(lst):
    for i in range(0, len(lst)-1):
        no_swap = True
        for y in range(0, len(lst)-i-1):
            if lst[y] > lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
                no_swap = False

        if no_swap is True:
            break
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        for y in range(i, 0, -1):
            if lst[y-1] > lst[y]:
                lst[y-1], lst[y] = lst[y], lst[y-1]

    print(lst)


def insertion_sort_one_swap(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        idx = i
        for y in range(i, 0, -1):
            if lst[y-1] > x:
                lst[y] = lst[y-1]
                idx = y-1
        if idx != i:
            lst[idx] = x

    print(lst)


insertion_sort([212,33,2,55,1,45,3,21,5])
insertion_sort_one_swap([212,33,2,55,1,45,3,21,5])