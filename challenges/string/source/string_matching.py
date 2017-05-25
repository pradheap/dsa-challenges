

def naive_string_matching(haystack, needle):
    t_length = len(haystack)
    p_length = len(needle)
    for i in range(t_length - p_length + 1):
        j = 0
        is_found = True
        for j in range(0, p_length):
            if needle[j] != haystack[i+j]:
                is_found = False
                break
        if is_found:
            return i
    return -1


def hash_func(s):
    prime_num = 7
    hash_value = 0
    for ind, char in enumerate(s):
        hash_value += ord(char) * pow(prime_num, ind)
    return hash_value


# A rolling hash doesn't loop through all characters in the string every time.
# It gets the char to be excluded and the char to be included and calculates the hash.
# So, for any huge part of the text, there are only two characters that are changing.
def _rolling_hash(prev_hash, prev_char, next_char, length):
    prime_num = 7
    hash_value = (prev_hash - ord(prev_char)) // prime_num
    return hash_value + ord(next_char) * pow(prime_num, length - 1)


def rabin_karp_string_matching(haystack, needle):
    t_length = len(haystack)
    p_length = len(needle)
    p_hash = hash_func(needle)
    t_hash = hash_func(haystack[0:len(needle)])
    if p_hash == t_hash:
        return 0
    for i in range(1, t_length - p_length + 1):
        t_hash = _rolling_hash(t_hash, haystack[i-1], haystack[i + p_length - 1], p_length)
        if p_hash == t_hash:
            return i