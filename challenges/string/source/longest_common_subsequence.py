

# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def longest_common_subsequence_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    seq = ''
    i = m
    j = n
    # No need to traverse through entire columns for each row. Traverse from
    # end to start columns also traversing through all the rows. If we've
    # reached the column 0 when on any row, just quit, we've got the longest sequence.
    while i > 0:
        if j == 0:
            break
        while j > 0:
            # Traversing to the previous column, same row
            if matrix[i][j] == matrix[i][j-1]:
                j -= 1
            # Traversing to the previous row, same column
            elif matrix[i][j] == matrix[i-1][j]:
                break
            # Traversing to the diagonally lower element.
            # That's when you add the letter to the sequence.
            elif matrix[i][j] == (matrix[i-1][j-1] + 1):
                seq += s1[i-1]
                break
            else:
                break
        i -= 1

    return seq[::-1]