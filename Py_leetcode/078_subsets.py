import sys
import os
import math
from collections import defaultdict
import copy

"""
    Given a set of distinct integers, nums, return all possible subsets.

    Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
    For example,
    If nums = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""
def subsets(nums):
    n = len(nums)
    if n < 2:
        return [nums] if n else []

    res = []
    subsets_help(sorted(nums), 0, [], res)
    return res

def subsets_help(nums, idx, selected, res):
    if idx == len(nums):
        res.append(list(selected))
        return

    selected.append(nums[idx])
    subsets_help(nums, idx + 1, selected, res)
    selected.pop()
    subsets_help(nums, idx + 1, selected, res)


#nums = [1, 2, 3]
#for s in subsets(nums):
#    print s
