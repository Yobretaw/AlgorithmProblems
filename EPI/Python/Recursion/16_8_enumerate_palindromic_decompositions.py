import sys
import os
import math


"""
    Compute all palindromic decompositions of a given string. For example, if s
    is '0204451881', then the decomposition '020', '44', '5', '1881' is palindromic,
    as is '020', '44', '5', '1', '88', '1'. However, '02044', '5', '1881' is not.
"""
def enumerate_palindromic_decompositions(s):
    if not s:
        return []

    res = []
    enumerate_palindromic_decompositions_help(s, 0, [], res)
    return res

def enumerate_palindromic_decompositions_help(s, idx, curr, res):
    if idx == len(s):
        res.append(list(curr))
        return

    for i in range(idx + 1, len(s) + 1):
        if is_palindrome(s[idx:i]):
            curr.append(s[idx:i])
            enumerate_palindromic_decompositions_help(s, i, curr, res)
            curr.pop()

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    for line in enumerate_palindromic_decompositions('0204451881'):
        print line

    #for line in enumerate_palindromic_decompositions('1111111111'):
    #    print line
