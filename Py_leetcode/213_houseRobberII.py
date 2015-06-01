import sys
import math
import imp
from collections import defaultdict

"""
    After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much
    attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
    Meanwhile, the security system for these houses remain the same as for those in the previous street.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can
    rob tonight without alerting the police.
"""
def rob_help(nums):
        n = len(nums)
        if n < 2:
            return 0 if not n else nums[0]

        prev = 0
        curr = nums[0]
        for i in range(1, n):
            tmp = max(prev + nums[i], curr)
            prev, curr = curr, tmp

        return curr

def rob(nums):
    n = len(nums)
    if n < 2:
        return 0 if not n else nums[0][0]

    nums = [(c, 0) for c in nums]
    nums[0] = (nums[0][0], 1)
    nums[-1] = (nums[-1][0], 1)

    prev = (0, False)
    curr = nums[0]
    for i in range(1, n):
        tmp = curr
        if prev[0] + nums[i][0] > curr[0]:
            curr = (prev[0] + nums[i][0], prev[1] + nums[i][1])
        prev = tmp

    # if both the first and the last house are robbed, try robbing only one of them and return the larger one
    if curr[1] == 2:
        return max(rob_help([c[0] for c in nums[1:]]), rob_help([c[0] for c in nums[:-1]]))
    else:
        return curr[0]



#print rob([1, 1])
#print rob([1, 2, 2])
#print rob([2, 3, 2])
#print rob([1, 2, 1, 1])
#print rob([1, 1, 1, 1])
#print rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
