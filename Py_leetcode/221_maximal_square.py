import sys
import heapq
from collections import defaultdict, deque


"""
    Given a 2D binary matrix filled with 0's and 1's, find the largest square
    containing all 1's and return its area.

    For example, given the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Return 4.
"""
def maximal_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    accu_mtx = [[[0, 0] for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            accu_mtx[i][j][0] = 0 if matrix[i][j] == '0' else \
                1 + (accu_mtx[i - 1][j][0] if i > 0 else 0)
            accu_mtx[i][j][1] = 0 if matrix[i][j] == '0' else \
                1 + (accu_mtx[i][j - 1][1] if j > 0 else 0)

    square_mtx = [[0 for j in range(n)] for i in range(m)]
    max_side_len = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '0':
                continue

            if i == 0 or j == 0:
                square_mtx[i][j] = 1
            else:
                square_mtx[i][j] = min(
                                accu_mtx[i][j][0],
                                accu_mtx[i][j][1],
                                square_mtx[i - 1][j - 1] + 1
                )
            max_side_len = max(max_side_len, square_mtx[i][j])

    return max_side_len ** 2


if __name__ == '__main__':
    matrix = ['0']
    print maximal_square(matrix)

    matrix = [
        '10100',
        '10111',
        '11101',
        '10010'
    ]
    print maximal_square(matrix)

    matrix = [
        '10100',
        '10111',
        '11111',
        '10010'
    ]
    print maximal_square(matrix)

    matrix = [
        '10111',
        '10111',
        '11111',
        '10010'
    ]
    print maximal_square(matrix)
