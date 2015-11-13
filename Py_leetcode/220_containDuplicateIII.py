import sys
import math
import imp
from collections import defaultdict, deque
import heapq

"""
    Given an array of integers, find out whether there are two distinct indices
    i and j in the array such that the difference between nums[i] and nums[j]
    is at most t and the difference between i and j is at most k.
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    if t < 0:
        return False

    n = len(nums)
    d = {}
    t += 1
    for i in range(n):
        if i > k:
            d.pop(nums[i - k - 1] / t)

        m = nums[i] / t
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < t:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < t:
            return True

        d[m] = nums[i]

    return False


#print contain_nearby_almost_duplicate([0], 0, 0)
#print contain_nearby_almost_duplicate([1], 1, 1)
#print contain_nearby_almost_duplicate([4, 2], 2, 1)
#print contain_nearby_almost_duplicate([-1, -1], 1, -1)
#print contain_nearby_almost_duplicate([-1, -1], 1, 0)
print contain_nearby_almost_duplicate([0, 10, 22, 15, 0, 5, 22, 12, 1, 5], 3, 3)
