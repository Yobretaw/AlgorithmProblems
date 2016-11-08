import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Design an algorithm for rotating an array A of n elements to the right by i positions. Do
    not use library functions implementing rotate.

    For example, rotate [1, 2, 3, 4, 5] by 3 positions results [3, 4, 5, 1, 2]
    ============================================================================================
"""
def rotate(A, i):
    n = len(A)

    if n < 2:
        return

    """
    First we rotate A[0:n - i - 1]
    """
    A[0:n - i] = reversed(A[0: n - i])

    """
    Then we rotate A[n - i: n - 1]
    """
    A[n - i : n] = reversed(A[n - i : n])

    """
    Now we rotate the whole array
    """
    A[:] = A[::-1]
    return

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(A)):
    rotate(A, 1)
    print A
