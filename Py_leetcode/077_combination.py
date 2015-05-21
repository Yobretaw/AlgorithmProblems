import sys
import os
import math
from collections import defaultdict
import copy

"""
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
"""
def combination(n, k):
    res = []
    combination_help(n, k, 0, [], res)
    return res

def combination_help(n, k, idx, selected, res):
    if len(selected) == k:
        res.append(list(selected))
        return

    if idx == n or len(selected) > k:
        return
    
    selected.append(idx + 1)
    combination_help(n, k, idx + 1, selected, res)
    selected.pop()
    combination_help(n, k, idx + 1, selected, res)

#for s in combination(4, 2):
#    print s
