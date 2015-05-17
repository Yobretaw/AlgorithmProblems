import sys
import os
import math
import imp
from collections import deque

"""
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    For example, given s = "aab",
    Return

      [
        ["aa","b"],
        ["a","a","b"]
      ]
"""
def partition(s):
    n = len(s)
    if n < 2:
        return [] if not n else [[s]]

    mtx = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        mtx[i][i] = 1

    for i in range(0, n - 1):
        mtx[i][i + 1] = 1 if s[i] == s[i + 1] else 0

    for k in range(3, n + 1):
        for i in range(0, n - k + 1):
            mtx[i][i + k - 1] = 1 if s[i] == s[i + k - 1] and mtx[i + 1][i + k - 2] else 0

    res = []
    dfs(s, mtx, 0, [], res)
    return res

def dfs(s, mtx, idx, curr, res):
    if idx == len(s):
        res.append(list(curr))
        return

    for i in range(idx, len(s)):
        if mtx[idx][i]:
            curr.append(s[idx:i + 1])
            dfs(s, mtx, i + 1, curr, res)
            curr.pop()
        

for line in partition('efe'):
    print line
