import sys
import os
import math

"""
    Given two binary strings, return their sum (also a binary string).

    For example,
    a = "11"
    b = "1"

    Return "100".
"""
def add_binary(a, b):
    m = len(a)
    n = len(b)
    a = a[::-1]
    b = b[::-1]

    res = []
    carry = 0
    for i in range(0, max(m, n)):
        val = carry + (int(a[i]) if i < m else 0) + (int(b[i]) if i < n else 0)
        carry = 1 if val > 1 else 0
        val %= 2
        res.append(str(val))

    if carry == 1:
        res.append('1')

    return ''.join(res[::-1])


#a = '11'
#b = '1'
#print add_binary(a, b)
