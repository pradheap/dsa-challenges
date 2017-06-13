

# http://www.cs.jhu.edu/~langmea/resources/lecture_notes/dp_and_edit_dist.pdf
def min_edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    matrix = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, n + 1):
        matrix[0][i] = i
    for i in range(1, m + 1):
        matrix[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
    return matrix[m][n]