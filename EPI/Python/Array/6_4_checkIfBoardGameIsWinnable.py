import sys
import os
import re
import math

"""
    ============================================================================================
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    
    Each element in the array represents your maximum jump length at that position.
    
    Determine if you are able to reach the last index.
    
    For example:
      A = [2,3,1,1,4], return true.
      A = [3,2,1,0,4], return false.
    ============================================================================================
"""
def is_winnable(A):
    n = len(A)

    rightMost = 0
    for i in range(0, n):
        if i > rightMost:
            return False
        elif rightMost >= n:
            return True

        rightMost = i + A[i] if i + A[i] > rightMost else rightMost

    return True

print is_winnable([2, 3, 1, 1, 4])
print is_winnable([3, 2, 1, 0, 4])



"""
    ==============================================================================================
    Variant 6.4.1: Write a function to compute the minimum number of steps needed to advance to the
    last location
    ==============================================================================================
"""
def min_steps(A):
    n = len(A)

    reached = 0      # the maximum distance that has been reached
    rightMost = 0    # the maximum distance can be reached by using (result + 1) steps
    result = 0
    for i in range(0, n):
        if i > rightMost:
            return -1

        if i > reached:
            reached = rightMost
            result += 1

        rightMost = i + A[i] if i + A[i] > rightMost else rightMost

    return result


print min_steps([2, 3, 1, 1, 4])
print min_steps([3, 2, 1, 0, 4])
