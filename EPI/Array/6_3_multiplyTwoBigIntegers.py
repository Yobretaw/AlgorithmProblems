import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function that takes two strings representing integers, and returns an integer repre-
    senting their product
    ============================================================================================
"""
def multiply(a, b):
    is_a_neg = 1 if a[0] == '-' else 0
    is_b_neg = 1 if b[0] == '-' else 0

    if is_a_neg:
        a = a[1:]

    if is_b_neg:
        b = b[1:]

    m = len(a)
    n = len(b)

    a = a[::-1]
    b = b[::-1]
    result = [0] * (m + n)
    for i in range(0, m):
        for j in range(0, n):
            result[i + j] += (ord(a[i]) - ord('0')) * (ord(b[j]) - ord('0'))
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] / 10
                result[i + j] %= 10

    if result[-1] == 0:
        result.pop()

    if is_a_neg ^ is_b_neg:
        result.append('-')
    return ''.join(map(str, result[::-1]))

a = 49734873214723897498327
b = -102938019238120938098210983
print int(multiply(str(a), str(b))) == a * b
