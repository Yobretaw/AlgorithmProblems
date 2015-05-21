import sys
import os
import math

"""
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

    Given an encoded message containing digits, determine the total number of ways to decode it.

    For example,
    Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

    The number of ways decoding "12" is 2.
"""
def decode_ways(s):
    if not s:
        return 0

    m = {}
    return f(s, 0, m)

def f(s, i, m):
    if i == len(s) - 1:
        return 0 if s[i] == '0' else 1
    if i >= len(s):
        return 1

    if i in m:
        return m[i]

    res = 0
    curr_val = int(s[i])
    next_val = int(s[i + 1])
    if curr_val == 0:
        res = 0
    elif curr_val <= 2:
        if next_val == 0 or curr_val == 2 and next_val > 6:
            res = f(s, i + 2, m)
        else:
            res = f(s, i + 1, m) + f(s, i + 2, m)
    else:
        res = f(s, i + 1, m)
    m[i] = res
    return res


def decode_ways_iterative(s):
    if not s or s[0] == '0':
        return 0

    # use n1 to record the number of ways to the index i, and n0 to record the number of ways to the index i-1
    n0 = 1
    n1 = 1
    for i in range(1, len(s)):
        tmp = n1

        curr = int(s[i])
        if curr == 0:
            n1 = 0
        if s[i - 1] == '2' and curr <= 6 or s[i - 1] == '1':
            n1 += n0
        if n1 == 0:
            return 0
        n0 = tmp

    return n1


#print decode_ways('0'), decode_ways_iterative('0')
#print decode_ways('100'), decode_ways_iterative('100')
#print decode_ways('01'), decode_ways_iterative('01')
#print decode_ways('123'), decode_ways_iterative('123')
#print decode_ways('301'), decode_ways_iterative('301')
#print decode_ways('1001'), decode_ways_iterative('1001')
