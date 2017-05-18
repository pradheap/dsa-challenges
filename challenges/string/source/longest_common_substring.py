

def common_substring_dp(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    longest = 0
    longest_x = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[j-1] == s2[i-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
                if matrix[i][j] > longest:
                    longest = matrix[i][j]
                    longest_x = j

    return s1[longest_x - longest: longest_x]
