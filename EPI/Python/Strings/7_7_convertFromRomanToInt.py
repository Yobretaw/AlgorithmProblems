import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function which takes as input a valid Roman number string s and returns the integer
    it corresponds to.
    ============================================================================================
"""
def roman_to_decimal(s):
    n = len(s)

    if n == 0:
        return 0

    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res = m[s[0]]
    for i in range(1, n):
        if m[s[i]] > m[s[i - 1]]:
            res -= 2 * m[s[i - 1]]
            res += m[s[i]]
        else:
            res += m[s[i]]

    return res

#print roman_to_decimal("XXXXXIIIIIIIII")
#print roman_to_decimal("LVIIII")
#print roman_to_decimal("LIX")


"""
    Variant 7.7.1: Write a function that takes as input a string of Roman number symbols and
    checks whether that string is valid.

    In this problem we give simplified rules for representing numbers in this system. Specifically,
    define a string over Roman number symbols to be a valid Roman number string if symbols appear
    in nonincreasing order, with the following exceptions allowed:

        - I can immediately procede V and X
        - X can immediately procede L and C
        - C can immediately procede D and M

    Back-to-back exceptions are not allowd, e.g., IXC is invalid, as is CDM.
"""
def is_valid_roman_num(s):
    n = len(s)

    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if n == 0:
        return True
    
    if n == 1:
        return s[0] in m.keys()
    
    for i in range(1, n - 1):
        _prev = m.get(s[i - 1])
        _curr = m.get(s[i])
        _next = m.get(s[i + 1])

        if not _prev or not _curr or not _next:
            return False
        elif _prev < _curr < _next:
            return False
        elif not can_adjacent(_prev, _curr) or not can_adjacent(_curr, _next):
            return False
        else:
            continue

    return True

def can_adjacent(prev, curr):
    if prev < curr and (not prev in [1, 10, 100] or (curr - prev) >= 10 * prev):
        return False

    return True

#print is_valid_roman_num("IXC")
#print is_valid_roman_num("CDM")
#print is_valid_roman_num("XXXXXIIIIIIIII")
#print is_valid_roman_num("LVIIII")
#print is_valid_roman_num("LIX")


"""
    Variant 7.7.2: Write a function that takes as input a positive integer n and returns
    the shortest valid simple Roman number string representing n.
"""
def decimal_to_roman(n):
        m = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL'
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        d = 1
        while 10 * d <= n:
            d *= 10

        res = ""
        while n > 0:
            curr = n / d
            if curr == 9:
                res += m[9 * d]
            elif curr >= 5:
                res += m[5 * d]
                res += m[d] * (curr - 5)
            elif curr == 4:
                res += m[4 * d]
            else:
                res += m[d] * curr

            n %= d
            d /= 10

        return res

#print decimal_to_roman(59)
