import sys
import math


"""
    Consider a sequence of integer-valued arrays, <A_0, A_1, ..., A_(n-1)> in
    which A_i consists of i + 1 entries. Such a sequence naturally corresponds
    to a triangle of numbers, similar to Pascal's triangle. Define a path to
    be a sequence of numbers in which adjacent numbers in the number of sequence
    correspond to numbers that are adjacent in the triangle of integers.

    Design a function that takes as input a sequence of integer-valued arrays,
    <A_0, A_1, ..., A_(n-1)> and returns the minimum weight path from the top
    number to a number in Row n.
"""
def find_min_weight_path(arrs):
        n = len(arrs)
        INT_MIN = -sys.maxint

        # t[i][j] represents the minimum weight path to row i, column j.
        # We then have t[i][j] = arr[i][j] + min(t[i - 1][j - 1], t[i][j - 1])
        t = [[INT_MIN for x in range(i + 1)] for i in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    t[i][j] = arrs[i][j]
                elif j == 0 or j == i:
                    t[i][j] = arrs[i][j] + (t[i - 1][j] if j == 0 else t[i - 1][j - 1])
                else:
                    t[i][j] = arrs[i][j] + min(t[i - 1][j - 1], t[i - 1][j])

        return min(t[-1])


if __name__ == '__main__':
    arrs = [
        [1],
        [2, 3]
    ]
    print find_min_weight_path(arrs)

    arrs = [
        [1],
    ]
    print find_min_weight_path(arrs)
