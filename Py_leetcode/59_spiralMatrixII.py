import sys
import os
import math

"""
    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,

    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
"""
def spiral_matrix_ii(n):
    if n < 2:
        return [[1]] if n else []

    start_x = 0
    start_y = 0
    end_x = n - 1
    end_y = n - 1
    val = 1
    mtx = [[0 for i in range(0, n)] for i in range(0, n)]
    while True:
        if start_x > end_x:
            break

        for i in range(start_x, end_x + 1):
            mtx[start_y][i] = val
            val += 1
        start_y += 1

        if start_y > end_y:
            break
        
        for i in range(start_y, end_y + 1):
            mtx[i][end_x] = val
            val += 1
        end_x -= 1

        if start_x > end_x:
            break

        for i in reversed(range(start_x, end_x + 1)):
            mtx[end_y][i] = val
            val += 1
        end_y -= 1

        if start_y > end_y:
            break

        for i in reversed(range(start_y, end_y + 1)):
            mtx[i][start_x] = val
            val += 1
        start_x += 1
    
    return mtx

#for line in spiral_matrix_ii(3):
#    print line
