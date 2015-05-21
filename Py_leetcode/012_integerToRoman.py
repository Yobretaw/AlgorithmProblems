import sys
import math

"""
    Given an integer, convert it to a roman numeral.

    Input is guaranteed to be within the range from 1 to 3999.
"""
def intToRoman(x):
    m = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    d = 10
    while d * 10 < x:
        d *= 10

    res = ''
    while x > 0:
        curr = x / d

        if curr in m:
            res += m[curr * d]
        else:
            if curr > 5:
                res += m[5 * d] + m[d] * (curr - 5)
            else:
                res += m[d] * curr
        x %= d
        d /= 10

    return res

#for i in range(1, 3000):
#    print intToRoman(i)
