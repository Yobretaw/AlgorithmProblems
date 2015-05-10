import sys
import os
import math
from collections import defaultdict
import copy

"""
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
    It doesn't matter what you leave beyond the new length.
"""
def remove_dup(arr):
        n = len(arr)

        if n < 3:
            return n

        write_idx = 2
        count = 2 if arr[1] == arr[0] else 1
        for i in range(2, n):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 0

            if count <= 2:
                arr[write_idx] = arr[i]
                write_idx += 1
                count += 1
        return write_idx


def remove_dup2(arr):
    n = len(arr)
    if n < 3:
        return n

    write_idx = 1
    for i in range(2, n):
        if arr[i] != arr[write_idx] or arr[write_idx] != arr[write_idx - 1]:
            write_idx += 1
            arr[write_idx] = arr[i]
    return write_idx + 1

arr = [1, 1, 1, 2, 2, 2, 3]
print remove_dup(arr), arr
