import sys
import os
import math

"""
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

    For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.

    click to show more practice.

    More practice:
    If you have figured out the O(n) solution, try coding another solution using the
    divide and conquer approach, which is more subtle.
"""
def largest_sum(arr):
    n = len(arr)
    
    if n < 2:
        return 0 if not n else arr[0]

    max_sum = arr[0]
    max_end_here = arr[0]
    for i in range(1, n):
        if max_end_here > 0:
            max_end_here += arr[i]
        else:
            max_end_here = arr[i]

        max_sum = max(max_sum, max_end_here)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print largest_sum(arr)
