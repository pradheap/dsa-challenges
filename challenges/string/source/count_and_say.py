

def count_and_say(s):
    prev = None
    result = []
    count = 1
    for i in s:
        if prev == i:
            count += 1
        elif prev:
            result.append(str(count))
            result.append(prev)
            count = 1
        prev = i
    result.append(str(count))
    result.append(prev)
    return ''.join(result)