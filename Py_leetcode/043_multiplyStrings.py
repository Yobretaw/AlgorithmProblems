import sys
import math
from collections import defaultdict

"""
    Given two numbers represented as strings, return multiplication of the numbers as a string.

    Note: The numbers can be arbitrarily large and are non-negative.
"""
def multiply_string(a, b):
    m = len(a)
    n = len(b)

    a = a[::-1]
    b = b[::-1]

    res = [0] * (m + n)
    for i in range(0, m):
        for j in range(0, n):
            res[i + j] += int(a[i]) * int(b[j])
            res[i + j + 1] += res[i + j] / 10
            res[i + j] %= 10

    i = len(res) - 1
    # note should be i >= 1 rather than i >= 0 since the result have length at least 1
    while i >= 1 and res[i] == 0:
        res.pop()
        i -= 1

    return ''.join([str(c) for c in res[::-1]])

#a = "123"
#b = "456"
#print multiply_string(a, b)
