import sys
import math
import imp
from collections import defaultdict, deque
import heapq

"""
    Given an array of integers, find out whether there are two distinct indices i and j in
    the array such that the difference between nums[i] and nums[j] is at most t and the difference
    between i and j is at most k.
"""
def contain_nearby_almost_duplicate(nums, k, t):
    if k < 1 or t < 0:
        return False

    m = {}
    for i in range(0, len(nums)):
        val = nums[i] + sys.maxint
        bucket = val / (t + 1)
        if bucket in m \
                or (bucket - 1 in m and val - m[bucket - 1] <= t) \
                or (bucket + 1 in m and m[bucket + 1] - val <= t):
            return True

        if len(m) >= k:
            last_bucket = (nums[i - k] + sys.maxint) / (t + 1)
            m.pop(last_bucket, None)

        m[bucket] = val

    return False


#print contain_nearby_almost_duplicate([0], 0, 0)
#print contain_nearby_almost_duplicate([1], 1, 1)
#print contain_nearby_almost_duplicate([4, 2], 2, 1)
#print contain_nearby_almost_duplicate([-1, -1], 1, -1)
#print contain_nearby_almost_duplicate([-1, -1], 1, 0)
print contain_nearby_almost_duplicate([0, 10, 22, 15, 0, 5, 22, 12, 1, 5], 3, 3)
