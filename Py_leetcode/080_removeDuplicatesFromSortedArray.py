import sys
import os
import math

"""
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array nums = [1, 1, 1, 2, 2, 3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
    It doesn't matter what you leave beyond the new length.
"""
def remove_dup(arr):
    n = len(arr)

    if n < 3:
        return n

    write_idx = 2
    for i in range(2, n):
        if arr[i] != arr[write_idx - 1] or arr[write_idx - 1] != arr[write_idx - 2]:
            arr[write_idx] = arr[i]
            write_idx += 1
    return write_idx


#arr = [1, 1, 1, 2, 2, 2, 3]
#arr = [1, 1, 1, 2, 2, 3]
#print remove_dup(arr), arr
