import sys
import os
import math

"""
    Call a 2D array sorted if its rows and columns are sorted in increasing
    sorted order.

    Design an algorith that takes a 2D sorted array and a number and checks
    whether that number appears in the array.
"""
def find_in_2d_array(mtx, x):
    m, n = len(mtx), len(mtx[0])

    i, j = 0, n - 1
    while 0 <= i < m and 0 <= j < n:
        print i, j
        if mtx[i][j] == x:
            return True
        elif mtx[i][j] < x:
            i += 1
        else:
            j -= 1
    return False

#mtx = [
#    [-1, 2, 4, 4, 6],
#    [1, 5, 5, 9, 21],
#    [3, 6, 6, 9, 22],
#    [3, 6, 8, 10, 24],
#    [6, 8, 9, 12, 25],
#    [8, 10, 12, 13, 40]
#]
#print find_in_2d_array(mtx, 40)
