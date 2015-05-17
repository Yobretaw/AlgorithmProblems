import sys
import math
from collections import defaultdict

"""
    Given an array of integers, every element appears twice except for one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
def single_number(nums):
    ret = 0
    for val in nums:
        ret ^= val
    return ret

#nums = [1, 2, 3, 2, 3, 1, 4]
#print single_number(nums)
