import sys
import os
import re
import math
import random


"""
    ============================================================================================
    Design an algorithm that creates uniformlly random permutation of [0, 1, 2, ..., n - 1]. You
    are given a random number generator that returns integers in the set [0, 1, ..., n - 1] with
    equal probability; use as few calls to it as possible.

    Note: iterating through an array A and swapping each with elements with another random 
    selected element does not generate all permutation of A with equal probability.
    ============================================================================================
"""
def generateRandomPermutation(n):
    A = [0] * n

    for i in range(0, n):
        A[i] = i

    generateSubsets(A, n)
    return A


"""
    From 6.16.sampleOfflineData
"""
def generateSubsets(A, k):
    n = len(A);

    if n < 2:
        return

    """
    The last k slots in A will be used to store the random set
    """
    for i in range(0, min(k, n - k)):
        next_pos = random.randint(0, n - i - 1)
        A[n - i - 1], A[next_pos] = A[next_pos], A[n - i - 1]

    if k > n / 2:
        A[:] = A[::-1]

