import sys
import math

"""
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Here are few examples.
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
"""
def search_insert(num, x):
    if not num:
        return 0

    low = 0
    high = len(num)
    while low < high:
        mid = low + (high - low) / 2
        if num[mid] == x:
            return mid
        elif num[mid] > x:
            high = mid
        else:
            low = mid + 1
    return low


#print search_insert([1,3,5,6], 5)
#print search_insert([1,3,5,6], 2)
#print search_insert([1,3,5,6], 7)
#print search_insert([1,3,5,6], 0)
