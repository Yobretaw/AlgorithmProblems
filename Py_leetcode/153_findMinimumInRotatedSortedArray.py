import sys
import os
import math

"""
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    You may assume no duplicate exists in the array.
"""
def find_min(nums):
    n = len(nums)

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) / 2
        if nums[start] > nums[end]:
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        else:
            return nums[start]

#a = [4, 5, 6, 7, -2, 0, 1, 2, 3]
#print find_min(a)
