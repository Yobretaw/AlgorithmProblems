import sys
import os
import math
from collections import defaultdict

"""
    Given a collection of integers that might contain duplicates, nums, return all possible subsets.

    Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

    For example,
    If nums = [1,2,2], a solution is:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
"""
def subsets2(nums):
    if not nums or len(nums) == 1:
        return [] if not nums else [nums, []]

    res = []
    nums.sort()
    subsets2_help(nums, 0, [], res)
    return res


def subsets2_help(nums, idx, curr, res):
    n = len(nums)

    if n == idx:
        res.append(list(curr))
        return

    next_idx = idx
    while next_idx < n and nums[next_idx] == nums[idx]:
        next_idx += 1

    subsets2_help(nums, next_idx, curr, res)
    
    i = idx
    while i < n and nums[i] == nums[idx]:
        curr.append(nums[i])
        subsets2_help(nums, next_idx, curr, res)
        i += 1

    for i in range(idx, next_idx):
        curr.pop()

nums = [1, 2, 2]
print(subsets2(nums))

