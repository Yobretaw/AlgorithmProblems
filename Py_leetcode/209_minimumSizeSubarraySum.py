import sys
import math
from collections import defaultdict

"""
    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s. If there isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.

    More practice:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
def min_subarray_len(s, nums):
    start = end = curr_sum = 0
    min_len = sys.maxint
    for end in range(len(nums)):
        curr_sum += nums[end]
        while curr_sum - nums[start] >= s:
            curr_sum -= nums[start]
            start += 1
        if curr_sum >= s:
            min_len = min(min_len, end - start + 1)
    return min_len if curr_sum >= s else 0


#a = [2, 3, 1, 2, 3, 4]
#a = [1, 4, 4]
#a = [1, 2, 3, 4, 5]
#print min_subarray_len(11, a)
