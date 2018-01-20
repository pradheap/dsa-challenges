This module contains solutions for most of the stack problems found
across the WWW ranging from sites such as hackerrank, geekforgeeks and other random sites.
Pep8 standard naming convention is followed.
The properties are accessed or mutated via getters and setters


CLASSES

    Stack
    problems - # Python Lists can be used as a stack ADT with similar Big O complexity.

    
    class Stack
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  is_empty(self)
     |  
     |  peek(self)
     |  
     |  pop(self)
     |  
     |  push(self, data)
     |  
     |  size(self)

FUNCTIONS

    balanced_parentheses(expr)
        Check whether a given expression is balanced parentheses wise.
        There are 3 cases for non-empty expressions:
            a. expression is balanced, open and closed parentheses are equal in number
            b. extra open/close parentheses but with matching parentheses in-between,
            so stack won't be empty at the end. Then, it's unbalanced.
            c. open and close parentheses counts are equal but, one or more of them are a mismatch.
        
        :param expr: input string that represents an expression.
        :return: a boolean value indicating the balanced-ness of the expression.
    
    convert_decimal_to_any_base(num, base)
        Convert a decimal number to any base such as binary, hex and octal.
        Mimics Python's inbuilt conversion functions.
        Octal prefix - 0, hex prefix - 0x, binary prefix - 0b
        Note- Just the prefix for Octal number 0 is nothing.
        
        :param num: decimal number we want to convert
        :param base: the base we want the decimal number to convert to
        :return: the decimal number converted to respective base.


