

def linear_traversal(arr):
    rows = len(arr)
    columns = len(arr[0])
    result = []
    # includes 0 and excludes rows
    for i in range(rows):
        for j in range(columns):
            result.append(arr[i][j])
    return result


def reverse_traversal(arr):
    rows = len(arr)
    columns = len(arr[0])
    result = []
    # includes rows-1 and excludes -1
    for i in range(rows-1, -1, -1):
        for j in range(columns-1, -1, -1):
            result.append(arr[i][j])

    return result


def zigzag_traversal(arr):
    rows = len(arr)
    columns = len(arr[0])
    result = []
    row_num = 1
    for i in range(rows):
        if row_num % 2 == 0:
            for j in range(columns-1, -1, -1):
                result.append(arr[i][j])
        else:
            for j in range(columns):
                result.append(arr[i][j])
        row_num += 1
    return result


def reverse_zigzag_traversal(arr):
    rows = len(arr)
    columns = len(arr[0])
    result = []
    row_num = 1
    for i in range(rows-1, -1, -1):
        if row_num % 2 == 0:
            for j in range(columns):
                result.append(arr[i][j])
        else:
            for j in range(columns - 1, -1, -1):
                result.append(arr[i][j])
        row_num += 1

    return result


def vertical_traversal(arr):
    rows = len(arr)
    cols = len(arr[0])
    for j in range(cols):
        for i in range(rows):
            print arr[i][j]


def reverse_vertical_traversal(arr):
    rows = len(arr)
    cols = len(arr[0])
    for j in range(cols - 1, -1, -1):
        for i in range(rows - 1, -1, -1):
            print arr[i][j]


def diagonal_traversal(arr):
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows + cols - 1):
        # optimization to limit the x and y increase/decrease
        row_min = max(0, i - rows + 1)
        row_max = min(i + 1, rows)

        for x in range(row_min, row_max):
            y = i - x
            if 0 <= y < cols:
                print arr[x][y]




# vertical_traversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# reverse_vertical_traversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diagonal_traversal([[0, 2, 9], [1, 3, 4], [12, 13, 10]])
