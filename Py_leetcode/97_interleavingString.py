import sys
import os
import math

"""
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

    For example,
    Given:
    s1 = "aabcc",
    s2 = "dbbca",

    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.
"""
def interleaving_string(s1, s2, s3):
    if not s1 or not s2:
        return s3 == s2 if s2 else s3 == s1

    if len(s1) + len(s2) != len(s3):
        return False

    m = len(s1)
    n = len(s2)

    f = [[False for i in range(0, n + 1)] for j in range(0, m + 1)]

    for i in range(0, m + 1):
        f[i][0] = s1[:i] == s3[:i]

    for j in range(0, n + 1):
        f[0][j] = s2[:j] == s3[:j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            f[i][j] = f[i - 1][j] and s1[i - 1] == s3[i + j - 1] or \
                      f[i][j - 1] and s2[j - 1] == s3[i + j - 1]
    return f[m][n]

def interleaving_string2(s1, s2, s3):
    if not s1 or not s2:
        return s1 == s3 if not s2 else s2 == s3

    if len(s1) + len(s2) != len(s3):
        return False

    m = len(s1)
    n = len(s2)
    f = [False] * (n + 1)
    for i in range(0, n + 1):
        f[i] = s2[:i] == s3[:i]

    for i in range(1, m + 1):
        f[0] = s1[:i] == s3[:i]
        for j in range(1, n + 1):
            f[j] = f[j] and s1[i - 1] == s3[i + j - 1] or \
                   f[j - 1] and s2[j - 1] == s3[i + j - 1]
    return f[-1]


#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbbcbcac"
#s3 = "aadbbbaccc"
#print interleaving_string(s1, s2, s3)
#print interleaving_string2(s1, s2, s3)
#print interleaving_string2('db', 'b', 'cbb')
