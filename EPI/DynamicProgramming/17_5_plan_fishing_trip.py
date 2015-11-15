import sys
import math

"""
    A fisherman is in a rectangle sea. The value of fish at point (i, j) in the
    sea is specified by a n x m matrix A.

    Write a program that computes the maximum value of fish a fishman can catch
    on a path from top-left to bottom-right. The fisherman can only move down
    or right.
"""
def compute_max_value(mtx):
    m, n = len(mtx), len(mtx[0])

    for i in range(m):
        for j in range(n):
            mtx[i][j] += max(
                    mtx[i - 1][j] if i > 0 else 0,
                    mtx[i][j - 1] if j > 0 else 0
                    )
    return mtx[-1][-1]


"""
    Variant 17.5.1

    Solve the same problem when the fishman can begin and end at any point. He
    must still move down or right. (Note that the value of fish may be negative)
"""
def compute_max_value_with_negative(mtx):
    m, n = len(mtx), len(mtx[0])

    max_val = -sys.maxint
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            mtx[i][j] += max(
                    mtx[i + 1][j] if i < m else 0,
                    mtx[i][j + 1] if j < n else 0
                    )
            max_val = max(max_val, mtx[i][j])
    return max_val


if __name__ == '__main__':
    pass
