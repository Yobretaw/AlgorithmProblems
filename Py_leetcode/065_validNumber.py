import sys
import os
import math

"""
    Validate if a given string is numeric.

    Some examples:

        "0" => true
        " 0.1 " => true
        "abc" => false
        "1 a" => false
        "2e10" => true

    Note: It is intended for the problem statement to be ambiguous. You should gather all
    requirements up front before implementing one.
"""
def valid_number(s):
    s = s.strip()

    n = len(s)

    if not n:
        return False

    i = 0
    if s[0] == '-' or s[0] == '+':
        i += 1

    num_digits = 0
    num_dots = 0
    while i < n and is_valid_char(s[i]):
        if s[i].isdigit():
            num_digits += 1
        else:
            num_dots += 1
        i += 1

    if (i < n and s[i] != 'e') or not num_digits or num_dots > 1:
        return False

    if i < n:
        i += 1
        num_digits = 0

    if i < n and (s[i] == '-' or s[i] == '+'):
        i += 1

    while i < n and s[i].isdigit():
        num_digits += 1
        i += 1

    return i == n and num_digits > 0

def is_valid_char(c):
    return c.isdigit() or c == '.'


#print valid_number('0')
#print valid_number('0e')
#print valid_number(' 0.1')
#print valid_number('.')
#print valid_number('abc')
#print valid_number('1 a')
#print valid_number('2e10')
