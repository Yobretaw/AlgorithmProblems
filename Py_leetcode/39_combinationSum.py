import sys
import math

"""
    Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).

    The solution set must not contain duplicate combinations.

    For example, given candidate set 2,3,6,7 and target 7, one solution set is: 

    [7] 
    [2, 2, 3] 
"""
def combination_sum(nums, target):
    if not nums:
        return []

    nums.sort()
    result = []
    combination_sum_help(nums, target, 0, [], result)
    return result

def combination_sum_help(nums, target, idx, curr, result):
    if target == 0:
        result.append(list(curr))
        return

    i = idx
    while i < len(nums) and nums[i] <= target:
        curr.append(nums[i])
        combination_sum_help(nums, target - nums[i], i, curr, result)
        curr.pop()
        i += 1


#nums = [2, 3, 6, 7]
#print combination_sum(nums, 7)
