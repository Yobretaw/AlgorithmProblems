import sys
import math
import imp
from sets import Set

"""
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    For example,
    Given [100, 4, 200, 1, 3, 2],
    The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

    Your algorithm should run in O(n) complexity.
"""
def longestConsecutive(nums):
    m = {}
    for val in nums:
        m[val] = 1

    max_len = 0
    for val in m:
        m[val] = 0
        curr_len = 1
        small = val - 1
        while small in m and m[small]:
            curr_len += 1
            m[small] = 0
            small -= 1
        large = val + 1
        while large in m and m[large]:
            curr_len += 1
            m[large] = 0
            large += 1
        max_len = max(max_len, curr_len)
    return max_len


#nums = [100, 4, 200, 1, 3, 2]
#print longestConsecutive(nums)
