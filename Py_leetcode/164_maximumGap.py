import sys
import math
from sets import Set

"""
    Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

    Try to solve it in linear time/space.

    Return 0 if the array contains less than 2 elements.

    You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
def maximum_gap(nums):
    nums = list(set(nums))
    n = len(nums)
    if n < 2:
        return 0

    max_val = max(nums)
    min_val = min(nums)
    interval = (max_val - min_val) / n
    container = [None] * n
    for i in range(0, n):
        container[i] = Set()
    
    for val in nums:
        idx = min((val - min_val) / interval, n - 1)
        container[idx].add(val)
    
    res = 0
    last = 0
    for i in range(0, n):
        if len(container[i]):
            res = max(res, min(container[i]) - max(container[last]))
            last = i
    return res



#print maximum_gap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740])
#print maximum_gap([3, 6, 9, 1])
#print maximum_gap([1,1,1,1,1,5,5,5,5,5])
#print maximum_gap([1, 2, 8, 4, 10, 3, 13, 33, 5])
