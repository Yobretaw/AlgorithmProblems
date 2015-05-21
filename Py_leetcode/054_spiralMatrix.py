import sys
import os
import math

"""
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    For example,
    Given the following matrix:

    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    You should return [1,2,3,6,9,8,7,4,5].
"""
def spiral_matrix(mtx):
    m = len(mtx)
    if m < 1:
        return

    n = len(mtx[0])

    res = []
    start_x = 0
    start_y = 0
    end_x = n - 1
    end_y = m - 1
    while True:
        if start_x > end_x:
            break

        for i in range(start_x, end_x + 1):
            res.append(mtx[start_y][i])

        start_y += 1
        if start_y > end_y:
            break

        for i in range(start_y, end_y + 1):
            res.append(mtx[i][end_x])

        end_x -= 1

        if start_x > end_x:
            break

        for i in reversed(range(start_x, end_x + 1)):
            res.append(mtx[end_y][i])

        end_y -= 1
        if start_y > end_y:
            break

        for i in reversed(range(start_y, end_y + 1)):
            res.append(mtx[i][start_x])

        start_x += 1

    return res

#mtx = [
#    [ 1, 2, 3 ],
#    [ 4, 5, 6 ],
#    [ 7, 8, 9 ]
#]
#print spiral_matrix(mtx)
