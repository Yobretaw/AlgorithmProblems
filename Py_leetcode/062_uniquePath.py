import sys
import os
import math

"""
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot
    is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
"""
def unique_path(m, n):
    seen = {}
    return unique_path_help(seen, 0, 0, m, n)

def unique_path_help(seen, i, j, m, n):
    if (i, j) in seen:
        return seen[(i, j)]

    if i == m - 1 and j == n - 1:
        return 1

    if i == m or j == n:
        return 0

    seen[(i, j)] = unique_path_help(seen, i + 1, j, m, n) + unique_path_help(seen, i, j + 1, m, n)
    return seen[(i, j)]


def unique_path2(m, n):
    return math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))

def unique_path3(m, n):
    path = [1] * n
    for i in range(0, m - 1):
        for j in range(1, n):
            path[j] += path[j - 1]
    return path[-1]


#print unique_path(10, 5)
#print unique_path2(10, 5)
print unique_path3(10, 5)
