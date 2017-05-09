# Python Lists can be used as a stack ADT with similar Big O complexity.


class Stack:

    def __init__(self):
        self.container = []

    def push(self, data):
        self.container.append(data)

    def peek(self):
        if self.is_empty():
            return None
        return self.container[len(self.container) - 1]

    def pop(self):
        if self.is_empty():
            return None
        return self.container.pop()

    def is_empty(self):
        return 0 == len(self.container)

    def size(self):
        return len(self.container)


def balanced_parentheses(expr):
    """
    Check whether a given expression is balanced parentheses wise.
    There are 3 cases for non-empty expressions:
        a. expression is balanced, open and closed parentheses are equal in number
        b. extra open/close parentheses but with matching parentheses in-between,
        so stack won't be empty at the end. Then, it's unbalanced.
        c. open and close parentheses counts are equal but, one or more of them are a mismatch.

    :param expr: input string that represents an expression.
    :return: a boolean value indicating the balanced-ness of the expression.
     """

    is_balanced = True
    index = 0
    stack = Stack()
    openers = '{[('
    closers = '}])'
    # Iterate over each char and break out if we find one instance of unbalanced parenthesis
    while index < len(expr) and is_balanced:
        # if it's one of the open parenthesis, push it to the stack.
        if expr[index] in openers:
            stack.push(expr[index])
        # else if the stack is empty,
        else:
            # An extra closer parentheses is still there in the expression.
            if stack.is_empty():
                is_balanced = False
            # If the opener and closer parenthesis matches, pop the opener tag out of the stack.
            elif openers.index(stack.peek()) == closers.index(expr[index]):
                stack.pop()
            else:
                is_balanced = False
        index += 1

    # Extra open parentheses is still there in the stack, but so far it's balanced
    if is_balanced and stack.is_empty():
        is_balanced = True
    else:
        is_balanced = False

    return is_balanced


def convert_decimal_to_any_base(num, base):
    """
    Convert a decimal number to any base such as binary, hex and octal.
    Mimics Python's inbuilt conversion functions.
    Octal prefix - 0, hex prefix - 0x, binary prefix - 0b
    Note- Just the prefix for Octal number 0 is nothing.

    :param num: decimal number we want to convert
    :param base: the base we want the decimal number to convert to
    :return: the decimal number converted to respective base.
    """
    digits = '0123456789ABCDEF'
    stack = Stack()
    while num > 0:
        stack.push(num % base)
        num /= base

    bin_num = ''
    if stack.is_empty():
        bin_num = '0'
    while not stack.is_empty():
        bin_num += str(digits[stack.pop()])
    prefix = ''
    if base == 2:
        prefix = '0b'
    elif base == 16:
        prefix = '0x'
    if base == 8 and bin_num != '0':
        prefix = '0'

    return prefix + bin_num



