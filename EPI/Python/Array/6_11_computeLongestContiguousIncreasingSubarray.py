import sys
import os
import re
import math


"""
    ============================================================================================
    Implement an algorithm that takes as input an array A of n elements, and returns the beginning
    and ending indices of a longest increasing subarray of A. Fo exmaple, if A = [2, 11, 3, 5, 13,
    7, 19, 17, 23], the longest increasing subarray is [3, 5, 13], and you should return (2, 4)
    ============================================================================================
"""
def computeLongestIncreasingSubarray(A):
    n = len(A)

    if n == 0:
        return (-1, -1)

    if n == 1:
        return (0, 0)


    start = 0
    end = 0
    max_start = 0
    max_end = 0

    max_len = 0
    curr_len = 0
    for i in range(1, n):
        if A[i] < A[i - 1]:
            curr_len = 1
            start = i
            end = i
        else:
            curr_len += 1
            end = i

        if curr_len > max_len:
            max_start = start
            max_end = end
            max_len = curr_len

    return max_start, max_end


l = [2, 11, 3, 5, 13, 7, 19, 17, 23]
print computeLongestIncreasingSubarray(l)
