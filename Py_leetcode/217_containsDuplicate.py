import sys
import math
import imp
from collections import defaultdict

"""
    Given an array of integers, find if the array contains any duplicates. Your function should return
    true if any value appears at least twice in the array, and it should return false if every element
    is distinct.
"""
def contain_duplicate(nums):
    m = set()
    for val in nums:
        if val in m:
            return True
        m.add(val)
    return False

def contain_duplicate2(nums):
    num.sorted()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
