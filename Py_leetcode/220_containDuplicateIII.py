import sys
import math
import imp
from collections import defaultdict

"""
    Given an array of integers, find out whether there are two distinct indices i and j in
    the array such that the difference between nums[i] and nums[j] is at most t and the difference
    between i and j is at most k.
"""
def contain_nearby_almost_duplicate(nums, k, t):
    nums = [(nums[i], i) for i in range(0, len(nums))]
    nums.sort(key=lambda x: x[0])

    print nums
    for i in range(1, len(nums)):
        if abs(nums[i][0] - nums[i - 1][0]) <= t and abs(nums[i][1] - nums[i - 1][1]) <= k:
            return True
    return False

print contain_nearby_almost_duplicate([0, 10, 22, 15, 0, 5, 22, 12, 1, 5], 3, 3)
