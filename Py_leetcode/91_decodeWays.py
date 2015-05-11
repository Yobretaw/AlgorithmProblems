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

    The number of ways decoding "12" is 2.
"""
def decode_ways(s):
    if not s or len(s) == 1:
        return 0 if not s else 1

    return decode_ways_help(s, 0)

def decode_ways_help(s, idx):
    n = len(s)
    if idx >= n:
        return 0

    curr_val = int(s[idx])
    if curr_val == 0:
        return decode_ways_help(s, idx + 1)
    elif curr_val == 1:
        return decode_ways_help(s, idx + 1) + decode_ways_help(s, idx + 2)
    elif curr_val == 2:
        if idx < n - 1 and int(s[idx + 1]) < 7:
            return decode_ways_help(s, idx + 1) + decode_ways_help(s, idx + 2)
        else:
            return decode_ways_help(s, idx + 2)
    else:
        return decode_ways_help(s, idx + 1)

print decode_ways('12')

