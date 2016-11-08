import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Implement an algorithm to rotate a,an NxN 2D array, by 90 degrees clockwise. Assume that
    N = 2^k for some positive k.
    ============================================================================================
"""
def rotateClockwise(A):
    n = len(A)

    for i in range(0, n/2):
        for j in range(0, n):
            A[i][j], A[n - i - 1][j] = A[n - i - 1][j], A[i][j]

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]


A = [
        [1, 2],
        [3, 4]
    ]
rotateClockwise(A)
print A
            
        
D = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
rotateClockwise(D)
print D
