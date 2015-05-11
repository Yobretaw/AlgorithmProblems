import sys
import os
import math

"""
    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
    containing all ones and return its area.
"""
def max_rectangle(mtx):
    m, n = len(mtx), len(mtx[0]) if mtx else 0
    if not m or not n:
        return 0
    
    H = [0] * n
    L = [0] * n
    R = [n] * n

    ret = 0
    for i in range(0, m):
        left, right = 0, n
        for j in range(0, n):
            if mtx[i][j] == '1':
                H[j] += 1
                L[j] = max(L[j], left)
            else:
                left = j + 1
                H[j] = 0
                L[j] = 0

        for j in reversed(range(0, n)):
            if mtx[i][j] == '1':
                R[j] = min(R[j], right)
                ret = max(ret, H[j] * (R[j] - L[j]))
            else:
                right = j
                R[j] = n

    return ret
