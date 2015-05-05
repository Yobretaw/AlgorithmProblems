import sys
import os
import math

"""
    Follow up for N-Queens problem.

    Now, instead outputting board configurations, return the total number of distinct solutions.
"""
def n_queens(n):
    curr = ['.'] * n
    res = [0]
    n_queens_help(0, curr, res)
    return res[0]


def n_queens_help(idx, curr, res):
    n = len(curr)
    if idx == n:
        res[0] += 1
        return True
    
    for x in range(0, n):
        if is_valid_put(curr, idx, x):
            curr[idx] = x
            n_queens_help(idx + 1, curr, res)
            curr[idx] = None


def is_valid_put(arr, idx, x):
    for i in range(0, idx):
        if arr[i] == x or arr[i] == x - idx + i or arr[i] == x + idx - i:
            return False
    return True

#print n_queens(10)
