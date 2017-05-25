

def wildcard_match(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    matrix = [[False] * (pattern_length + 1) for i in range(text_length + 1)]
    matrix[0][0] = True
    for i in range(1, text_length + 1):
        for j in range(1, pattern_length + 1):
            if text[i-1] == pattern[j-1] or pattern[j-1] == '?':
                matrix[i][j] = matrix[i-1][j-1]
            elif pattern[j-1] == '*':
                if j-1 == 0 and i-1 == 0:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = matrix[i-1][j] or matrix[i][j-1]
            else:
                matrix[i][j] = False
    return matrix[text_length][pattern_length]