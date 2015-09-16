import sys
import os
import math
import random
import imp
from heapq import *
import collections

select = imp.load_source('select', '../Util/quick_select.py').select

"""
    The goal of this problem if to design an algorithm for computing the k-th
    largest element in a sequence of elements that is presented one element
    at a time. The length of the sequence is not known in advance, and could
    be very large.

    Design an algorithm for computing the k-th largest element in a sequence
    of elements.
"""
def find_kth_largest_element(next_val, k):
    if not func_get_next_num():
        return None

    i = 0
    h = []
    for val in next_val:
        h.append(val)
        if len(h) == k:
            break
    
    heapify(h)
    for val in next_val:
        if val < h[0]:
            pass
        
        heappushpop(h, val)

    return h[0]


"""
    By using 2k - 1 as the array size, the time complexity of the selection algorithm is O(k).
    It is run every k - 1 elements, implying an O(n) time complexity.

    The space complexity is O(k)
"""
def find_kth_largest_element2(next_val, k):
    candidates = []
    for val in next_val:
        candidates.append(-val)
        if len(candidates) == k * 2 - 1:
            # reorders elements about median with larger elements appearing
            # before the median
            select(candidates, k - 1)

    select(candidates, k - 1)
    return -candidates[k - 1]


def func_get_next_num():
    nums = random.sample([i for i in range(1000)], 1000)
    for i in nums:
        yield nums[i]


for i in range(1000):
    print find_kth_largest_element2(func_get_next_num(), 100)

#for i in range(2000):
#    nums = random.sample([x + 1 for x in range(2000)], 2000)
#    if i + 1 != select(nums, i):
#        print i + 1
