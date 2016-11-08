import sys
import os
import re
import math

"""
    ============================================================================================
    Implement a string/integer inter-conversion function
    ============================================================================================
"""
def convert(x):
    if isinstance(x, str):
        return strToInt(x)
    elif isinstance(x, int):
        return intToStr(x)
    else:
        return None

def strToInt(s):
    val = 0
    sign = 1
    
    for c in s:
        if c == '-':
            sign = -1
        else:
            val *= 10
            val += (ord(c) - ord('0'))

    return sign * val


def intToStr(x):
    ret = ""
    sign = 1

    if x == 0:
        return "0"

    if x < 0:
        x = -x
        sign = -1

    while x > 0:
        ret += chr((x % 10) + ord('0'))
        x /= 10

    if sign < 0:
        ret += '-'

    return ret[::-1]


print convert(0)
print convert(1)
print convert(-1)
print convert(100)
print convert(-100)


print convert("0")
print convert("1")
print convert("-1")
print convert("100")
print convert("-100")
