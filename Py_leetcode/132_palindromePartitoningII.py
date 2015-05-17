import sys
import os
import math
import imp
from collections import deque
from sets import Set

"""
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return the minimum cuts needed for a palindrome partitioning of s.

    For example, given s = "aab",
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
def minCut(s):
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

    m = {}
    return dfs(s, mtx, 0, m)
    
    """
        BFS...
    """
    #level = 0
    #curr_level = Set()
    #next_level = Set()
    #curr_level.add(0)
    #while True:
    #    for i in curr_level:
    #        for j in reversed(range(i, n)):
    #            if mtx[i][j] and not j + 1 in next_level:
    #                next_level.add(j + 1)

    #    if n in next_level:
    #        return level
    #    curr_level = next_level
    #    next_level = Set()
    #    level += 1

def dfs(s, mtx, idx, m):
    if idx >= len(s) - 1:
        return 0
    if idx in m:
        return m[idx]

    res = sys.maxint
    for i in range(idx, len(s)):
        #print idx, i, mtx[idx][i]
        if mtx[idx][i]:
            res = min(res, dfs(s, mtx, i + 1, m))
    m[idx] = 1 + res if not mtx[idx][len(s) - 1] else res
    return m[idx]


#print minCut('ababa')
