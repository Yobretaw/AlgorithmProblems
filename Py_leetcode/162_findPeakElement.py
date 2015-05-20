import sys
import math

"""
    A peak element is an element that is greater than its neighbors.

    Given an input array where num[i] != num[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    You may imagine that num[-1] = num[n] = -infi

    For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

    Note:
    Your solution should be in logarithmic complexity.
"""
def find_peak_element(nums):
    n = len(nums)
    if n < 2:
        return 0 if n else -1

    start = 0
    end = n
    while start < end:
        mid = (start + end) / 2
        left = nums[mid] > nums[mid - 1] if mid > 0 else True
        right = nums[mid] > nums[mid + 1] if mid < n - 1 else True
        if left and right:
            return mid
        elif left:
            start = mid + 1
        else:
            end = mid
    return -1

#a = [1, 2, 3, 1]
#a = [1, 2]
#print find_peak_element(a)
