import sys
import os
import re
import math

"""
    ============================================================================================
    Implement a function for reversing the words in a string s. Assume s is stored in a array
    of characters
    ============================================================================================
"""
def reverse(s):
    n = len(s)

    if n < 2:
        return s

    s[:] = s[::-1]

    curr = 0
    while curr < n:
        while curr < n and s[curr].isspace():
            curr += 1

        start = curr
        while curr < n and not s[curr].isspace():
            curr += 1

        s[start:curr] = s[start:curr][::-1]


s = [c for c in "Alice likes Bob"]

reverse(s)
print ''.join(s)
