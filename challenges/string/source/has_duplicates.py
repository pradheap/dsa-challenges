from collections import Counter


def has_duplicates(s):
    return not len(set(s)) == len(s)


def has_duplicates_v1(s):
    count = Counter()
    for c in s:
        if count[c] > 0:
            return True
        else:
            count[c] += 1

    return False
