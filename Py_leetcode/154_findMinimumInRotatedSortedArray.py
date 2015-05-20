import sys
import os
import math

"""
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    The array may contain duplicates.
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
        elif nums[start] == nums[end]:
            end -= 1
        else:
            return nums[start]
    return nums[start]

#a = [4, 5, 6, 7, 7, 8, 8, 0, 2, 2]
#a = [3, 1, 3]
#print find_min(a)

