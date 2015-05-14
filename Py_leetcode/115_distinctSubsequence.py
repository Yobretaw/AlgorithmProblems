import sys
import os
import math
import imp
from collections import deque

"""
    Given a string S and a string T, count the number of distinct subsequences of S that equals to T

    A subsequence of a string is a new string which is formed from the original string by deleting
    some (can be none) of the characters without disturbing the relative positions of the remaining
    characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

    Here is an example:
    S = "rabbbit", T = "rabbit"

    Return 3.
"""
def num_distince(s, t):
    if not s or not t:
        return 1 if not t else 0

    m, n = len(s), len(t)

    # f[i][j] is the nubmer of distinct subsequence of s[:i] and t[:j]
    f = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]
    for i in range(0, m + 1):
        f[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            f[i][j] = f[i - 1][j] + (f[i - 1][j - 1] if s[i - 1] == t[j - 1] else 0)

    return f[-1][-1]


def num_distince2(s, t):
    if not s or not t:
        return 1 if not t else 0

    m, n = len(s), len(t)
    
    f = [0 for j in range(0, n + 1)]
    f[0] = 1

    for i in range(1, m + 1):
        g = list(f)
        for j in range(1, n + 1):
            f[j] += g[j - 1] if s[i - 1] == t[j - 1] else 0
        g = f
    return f[-1]


#s = "rabbbit"
#t = "rabbit"
#print num_distince(s, t)
#print num_distince2(s, t)
