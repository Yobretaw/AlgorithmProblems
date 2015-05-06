import sys
import os
import math

"""
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.

    For example:
    A = [2,3,1,1,4], return true.

    A = [3,2,1,0,4], return false.
"""
def jump_game(arr):
    n = len(arr)

    if n < 2:
        return True

    max_right = 0
    for i in range(0, n):
        if i > max_right:
            return False

        max_right = max(max_right, i + arr[i])
    return True
