import sys
import os
import math

"""
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""
def set_matrix_zeros(mtx):
    m = len(mtx)
    if not m:
        return
    n = len(mtx[0])
    if not n:
        return

    first_col_zero = False
    first_row_zero = False
    for i in range(0, m):
        if not mtx[i][0]:
            first_row_zero = True

    for j in range(0, n):
        if not mtx[0][j]:
            first_col_zero = True

    for i in range(1, m):
        for j in range(1, n):
            if not mtx[i][j]:
                mtx[i][0] = 0
                mtx[0][j] = 0

    for i in range(1, m):
        if not mtx[i][0]:
            for j in range(0, n):
                mtx[i][j] = 0

    for j in range(1, n):
        if not mtx[0][j]:
            for i in range(0, m):
                mtx[i][j] = 0

    if first_row_zero:
        for i in range(0, m):
            mtx[i][0] = 0

    if first_col_zero:
        for j in range(0, n):
            mtx[0][j] = 0


#mtx = [[0, 1]]
#mtx = [
#        [0, 0, 0, 5],
#        [4, 3, 1, 4],
#        [0, 1, 1, 4],
#        [1, 2, 1, 3],
#        [0, 0, 1, 1]
#]
#set_matrix_zeros(mtx)
#for line in mtx:
    #print line
