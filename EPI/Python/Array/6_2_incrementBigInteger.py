import sys
import os
import re
import math


"""
    ============================================================================================
    Write a function which takes as input an array A of digits encoding a deciaml number D and
    updates A to represent the number D + 1. For example, if A = [1, 2, 9] then you should update
    A to [1, 3, 0]
    ============================================================================================
"""
def increment(A):
    n = len(A)

    if n == 0:
        return [1]

    A[n - 1] += 1
    i = n - 1
    while i > 0 and A[i] == 10:
        A[i - 1] += 1
        A[i] = 0
        i -= 1

    if A[0] >= 10:
        A[0] = 0
        A.insert(0, 1)


A = [9, 9, 9, 9, 9, 9]
increment(A)
print A
