import sys
import math

"""
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of
    characters. No two characters may map to the same character but a character may map to itself.

    For example,
    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    Given "paper", "title", return true.

    Note:
    You may assume both s and t have the same length.
"""
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    elif s == t:
        return True

    # char -> idx
    ds = {}
    dt = {}
    for i in range(len(s)):
        a = s[i]
        b = t[i]

        idx_s = ds[a] if a in ds else -1
        idx_t = dt[b] if b in dt else -1

        if idx_s < 0 and idx_t < 0:
            ds[a] = dt[b] = i
        elif idx_s != idx_t:
            return False

    return True

#print is_isomorphic("aba", "baa")
#print is_isomorphic("egg", "add")
#print is_isomorphic("foo", "bar")
#print is_isomorphic("paper", "title")
#print is_isomorphic("baa", "cfa")
