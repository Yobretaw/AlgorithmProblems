import sys
import os
import math
from collections import defaultdict
import copy

"""
    Given a string S and a string T, find the minimum window in S which will contain all
    the characters in T in complexity O(n).

    For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC".

    Note:
    If there is no such window in S that covers all characters in T, return the emtpy string "".

    If there are multiple such windows, you are guaranteed that there will always be only one
    unique minimum window in S.
"""
def min_window_substring(s, t):
    if not s:
        return ''

    d = defaultdict(int)    # expected_count
    a = defaultdict(int)    # appeared_count

    for c in t:
        d[c] += 1

    min_width = sys.maxint
    min_start = start = 0
    appeared = 0
    for end in range(0, len(s)):
        if s[end] in d and d[s[end]] > 0:
            a[s[end]] += 1
            if a[s[end]] <= d[s[end]]:
                appeared += 1

        if appeared == len(t):
            while start < len(s) and (a[s[start]] > d[s[start]] or d[s[start]] == 0):
                a[s[start]] -= 1
                start += 1
            if min_width > (end - start + 1):
                min_width = end - start + 1
                min_start = start
    return s[min_start:min_start + min_width] if min_width != sys.maxint else ''


s = "ADOBECODEBANC"
t = "ABC"
print min_window_substring(s, t)
