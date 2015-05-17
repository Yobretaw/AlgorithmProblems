import sys
import os
import math
import imp

"""
    Given a triangle, find the minimum path sum from top to bottom. Each step you may
    move to adjacent numbers on the row below.

    For example, given the following triangle
    [
      [2],
      [3,4],
      [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total
    number of rows in the triangle.
"""
def minimumTotal(t):
    n = len(t)
    if n < 2:
        return 0 if not n else t[0][0]

    for i in range(1, n):
        t[i][0] += t[i - 1][0]
        for j in range(1, len(t[i]) - 1):
            t[i][j] += min(t[i - 1][j - 1] if j > 0 else 0, t[i - 1][j] if j < i else 0)
        t[i][-1] += t[i - 1][-1]
    return min(t[-1])


t = [
    #[-1],
    #[-2, -3]
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]

print minimumTotal(t)
