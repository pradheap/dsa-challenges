def factorial(n):
    if n == 0:
        return 1
    elif n <= 2:
        return n
    return n * factorial(n-1)

def bunny_ears(n):
    if n == 0:
        return 0
    return 2 + bunny_ears(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def bunny_ears2(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 3 + bunny_ears2(n-1)
    return 2 + bunny_ears2(n-1)

def triangle(n):
    if n <= 1:
        return n
    return n + triangle(n-1)

def count_7(n):
    if n == 0:
        return 0
    if (n % 10) == 7:
        return 1 + count_7(n // 10)
    return count_7(n // 10)

def count_8(n):
    if n == 0:
        return 0
    if (n % 10) == 8:
        if (n % 100) == 88:
            return 2 + count_8(n // 10)
        return 1 + count_8(n // 10)
    return count_8(n // 10)

def power_n(base, power):
    if power == 0:
        return 1
    if base == 0:
        return 0
    return base * power_n(base, power - 1)

def count_x(txt):
    if len(txt) == 0:
        return 0
    if txt[len(txt) - 1] == 'x':
        return 1 + count_x(txt[:len(txt) - 1])
    return count_x(txt[:len(txt) - 1])

def count_hi(txt):
    if len(txt) <= 1:
        return 0
    if txt[len(txt) - 2:] == 'hi':
        return 1 + count_hi(txt[:len(txt) - 2])
    return count_hi(txt[:len(txt) - 1])

def change_x_y(txt):
    if len(txt) == 0:
        return ""
    if txt[0] == 'x':
        return 'y' + change_x_y(txt[1:])
    return txt[0] + change_x_y(txt[1:])

def change_pi(txt):
    if len(txt) == 0:
        return ''
    if txt[:2] == 'pi':
        return '3.14' + change_pi(txt[2:])
    return txt[:1] + change_pi(txt[1:])

def no_x(txt):
    if len(txt) == 0:
        return ''
    if txt[0] == 'x':
        return no_x(txt[1:])
    return txt[0] + no_x(txt[1:])

def array_6(arr, idx):
    if idx >= len(arr) or idx < 0 or len(arr) == 0:
        return False
    if arr[idx] == 6:
        return True
    return array_6(arr, idx + 1)

def array_220(arr, idx):
    if idx + 1 >= len(arr) or idx < 0 or len(arr) <= 1:
        return False
    if arr[idx + 1] == arr[idx] * 10:
        return True
    return array_220(arr, idx + 1)

def all_star(txt):
    if len(txt) == 0:
        return ''
    if len(txt) == 1:
        return txt
    return txt[0] + '*' + all_star(txt[1:])

def pair_star(txt):
    if len(txt) == 0:
        return ''
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return txt[0] + '*' + pair_star(txt[1:])
    return txt[0] + pair_star(txt[1:])

def end_x(txt):
    if len(txt) == 0:
        return ''
    if txt[0] == 'x':
        return end_x(txt[1:]) + 'x'
    return txt[0] + end_x(txt[1:])

def count_pairs(txt):
    if len(txt) <= 2:
        return 0
    if txt[0] == txt[2]:
        return 1 + count_pairs(txt[1:])
    return 0 + count_pairs(txt[1:])

def string_clean(txt):
    if len(txt) == 0:
        return ''
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return string_clean(txt[1:])
    else:
        return txt[0] + string_clean(txt[1:])

def parent_bit(txt):
    if len(txt) == 0:
        return ''
    if txt[0] != '(':
        return parent_bit(txt[1:])
    if txt[len(txt) - 1] != ')':
        return parent_bit(txt[:len(txt) - 1])
    return txt

def nest_paren(txt):
    if len(txt) <= 1:
        return False
    if txt[0] == '(' and txt[len(txt) - 1] == ')':
        if len(txt) == 2:
            return True
        return True and nest_paren(txt[1:len(txt) - 1])
    return False

def str_count(txt, word):
    if len(word) > len(txt):
        return 0
    if txt[0:len(word)] == word:
        return 1 + str_count(txt[len(word):], word)
    return str_count(txt[1:], word)

def str_copies(txt, word, count):
    if len(word) > len(txt):
        return count == 0
    if txt[0:len(word)] == word:
        return str_copies(txt[len(word):], word, count - 1)
    return str_copies(txt[1:], word, count)

def str_dist(txt, word):
    if len(word) > len(txt):
        return 0
    if txt[0:len(word)] != word:
        return str_dist(txt[1:], word)
    if txt[len(txt) - len(word):] != word:
        return str_dist(txt[:len(txt) - 1], word)
    return len(txt)
    

