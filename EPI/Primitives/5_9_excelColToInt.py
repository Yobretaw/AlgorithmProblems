import sys
import os
import re
import math

"""
    The problem is similar to the problem of converting a string represening
    a base-26 number to the corresponding integer, except that 'A' corresponds
    to 1.
"""
def colToInt(s):
    ret = 0
    for c in s:
        ret = ret * 26 + ord(c) - ord('A') + 1
    return ret

def intToCol(val):
    ret = ""
    while val > 0:
        val -= 1
        ret += chr((val % 26) + ord('A'))
        val /= 26

    return ret[::-1]


print colToInt("A")
print colToInt("B")
print colToInt("Z")
print colToInt("AA")
print colToInt("AZ")
print colToInt("ZZ")
print "-"*50
print intToCol(colToInt("A"))
print intToCol(colToInt("B"))
print intToCol(colToInt("Z"))
print intToCol(colToInt("AA"))
print intToCol(colToInt("AZ"))
print intToCol(colToInt("ZZ"))
print intToCol(colToInt("ZZZZZ"))
