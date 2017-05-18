

def reverse_string(s):
    if s is '':
        return s

    return s[-1] + reverse_string(s[:-1])


def reverse_string_v1(s):
    new_str = ''
    for i in range(len(s), 0, -1):
        new_str += s[i-1]

    return new_str

