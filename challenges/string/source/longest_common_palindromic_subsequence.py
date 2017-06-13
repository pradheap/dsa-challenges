

def longest_common_palindromic_subsequence(s1):
    m = len(s1)
    matrix = [[0] * m for i in range(m)]
    for i in range(m):
        matrix[i][i] = 1
    result = []
    for sub_length in range(2, m + 1):
        for i in range(0, m - sub_length + 1):
            j = i + sub_length - 1
            if sub_length == 2 and s1[i] == s1[j]:
                matrix[i][j] = 2
            elif s1[i] == s1[j]:
                matrix[i][j] = 2 + matrix[i + 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1])

    i = 0
    j = m - 1
    while i < m:
        if j == 0:
            break
        while j > 0:
            idx = len(result) // 2
            # If the palindromic sequence was odd in length, it would be 1 -> 3 diagonally
            if matrix[i][j] == 1:
                result.insert(idx, s1[i])
                j = 0
                break
            # If the palindromic sequence was even in length, it would be 0 -> 2 diagonally
            elif matrix[i][j] == 0:
                j = 0
                break
            # If the characters are equal, move down diagonally.
            elif s1[i] == s1[j]:
                result.insert(idx, s1[i])
                result.insert(idx, s1[j])
                j -= 1
                break
            # If the characters are not equal, either move below on the same column or
            #  move backward on the same row.
            elif matrix[i][j] == matrix[i][j - 1]:
                j -= 1
            elif matrix[i][j] == matrix[i + 1][j]:
                i += 1
        i += 1
    return ''.join(result)