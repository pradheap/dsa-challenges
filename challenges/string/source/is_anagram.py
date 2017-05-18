from collections import Counter


def is_anagram(str1, str2):
    counts = Counter()
    for c in str1:
        counts[c.lower()] += 1

    for c in str2:
        counts[c.lower()] -= 1

    for key, value in counts.items():
        if value != 0:
            return False

    return True
