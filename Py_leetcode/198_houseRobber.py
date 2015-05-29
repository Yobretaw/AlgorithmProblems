import sys
import os
import re
import math

"""
    You are a professional robber planning to rob houses along a street. Each house has a certain amount
    of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have
    security system connected and it will automatically contact the police if two adjacent houses were broken
    into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum
    amount of money you can rob tonight without alerting the police.
"""
def rob(nums):
    n = len(nums)
    if n < 2:
        return 0 if not n else nums[0]
        
    prev, curr = 0, nums[0]
    max_val = 0
    for i in range(1, len(nums)):
        max_val = max(prev + nums[i], curr)
        prev, curr = curr, max_val
    return max_val

nums = [2, 1, 1, 2]
print rob(nums)
