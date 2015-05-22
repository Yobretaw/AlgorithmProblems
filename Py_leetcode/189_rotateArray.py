import sys
import os
import re
import math

"""
    Rotate an array of n elements to the right by k steps.

    For example, with n = 7 and k = 3, the array [1, 2, 3, 4, 5, 6, 7] is rotated to [5 ,6, 7, 1, 2, 3, 4]
"""
def rotate(nums, k):
    k %= len(nums)
    if not nums or k < 1:
        return

    nums[:-k] = nums[:-k][::-1]
    nums[-k:] = nums[-k:][::-1]
    nums[:] = nums[::-1]

#arr = [1, 2, 3, 4, 5, 6, 7]
#rotate(arr, 6)
#print arr
