import sys
import math
import imp
from collections import defaultdict

"""
    Given an array of integers and an integer k, find out whether there there are two distinct
    indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
def contain_nearby_duplicate(nums, k):
    m = {}
    for i in range(0, len(nums)):
        val = nums[i]
        if val in m and abs(m[val] - i) <= k:
            return True
        m[val] = i
    return False
