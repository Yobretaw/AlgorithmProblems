import sys
import os
import math
from collections import defaultdict
import copy

"""
    Follow up for "33. Search in Rotated Sorted Array":

    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

    Write a function to determine if a given target is in the array.


    ========================================================================
                33. Search in a Rotated Sorted Array

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
    ========================================================================
"""
def search_rotated_array(arr, k):
        n = len(arr)
        if n < 2:
            return True if arr[0] == k else False

        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) / 2
            if arr[mid] == k:
                return True
            elif arr[mid] < arr[end]:
                if arr[mid] < k <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif arr[mid] > arr[end]:
                if arr[start] <= k < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
        return False

arr = [4, 5, 5, 6, 7, 0, 0, 1, 1, 2]
#arr = [1, 1, 3, 1]
print search_rotated_array(arr, 0)

