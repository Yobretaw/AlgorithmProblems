import sys
import os
import math

"""
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    For example,

    Consider the following matrix:

    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    Given target = 3, return true.
"""
def search_matrix(mtx, k):
    m = len(mtx)
    if not m:
        return False

    n = len(mtx[0])
    if not n:
        return False

    i = 0
    j = n - 1
    while i < m and j >= 0:
        if mtx[i][j] == k:
            return True
        elif mtx[i][j] > k:
            j -= 1
        else:
            i += 1
    return False


#mtx = [
#      [1,   3,  5,  7],
#      [10, 11, 16, 20],
#      [23, 30, 34, 50]
#]
#mtx = [[1], [3]]
#print search_matrix(mtx, 3)
