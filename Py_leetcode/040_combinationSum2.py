import sys
import math
from collections import defaultdict

"""
    Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

    Each number in C may only be used once in the combination.

    Note:

        - All numbers (including target) will be positive integers.

        - Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <=  ak).

        - The solution set must not contain duplicate combinations.

    For example, given candidate set 10,1,2,7,6,1,5 and target 8, one solution set is: 

    [1, 7] 
    [1, 2, 5] 
    [2, 6] 
    [1, 1, 6] 
"""
def combination_sum_ii(nums, target):
    count_map = defaultdict(int)
    for val in nums:
        count_map[val] += 1

    res = []
    nums.sort()
    combination_sum_ii_help(nums, target, 0, [], count_map, res)
    return res

def combination_sum_ii_help(nums, target, idx, curr, count_map, res):
    if target == 0:
        res.append(list(curr))
        return

    i = idx
    if count_map[nums[i]] == 0:
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1

    while i < len(nums) and nums[i] <= target:
        curr.append(nums[i])
        count_map[nums[i]] -= 1
        combination_sum_ii_help(nums, target - nums[i], i, curr, count_map, res)
        count_map[nums[i]] += 1
        curr.pop()
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]: i += 1


#nums = [10, 1, 2, 7, 6, 1, 5]
#print combination_sum_ii(nums, 8)
