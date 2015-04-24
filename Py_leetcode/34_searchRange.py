import sys
import math

"""
    Given a sorted array of integers, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
"""
def search_range(num, x):
    if not num:
        return [-1, -1]
    
    return [find_min(num, x), find_max(num, x)]

def find_min(num, x):
    low = 0
    high = len(num)

    while low < high:
        mid = low + (high - low) / 2
        if num[mid] == x:
            if mid == 0 or num[mid - 1] != x:
                return mid
            else:
                high = mid
        elif num[mid] > x:
            high = mid
        else:
            low = mid + 1
    return -1

def find_max(num, x):
    low = 0
    high = len(num)
    n = len(num)
    while low < high:
        mid = low + (high - low) / 2
        if num[mid] == x:
            if mid == n - 1 or num[mid + 1] != x:
                return mid
            else:
                low = mid + 1
        elif num[mid] > x:
            high = mid
        else:
            low = mid + 1
    return -1

#num = [5, 7, 7, 8, 8, 10]
#print search_range(num, 10)
