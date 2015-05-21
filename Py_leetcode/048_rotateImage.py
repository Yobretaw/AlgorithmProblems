import sys
import math
from collections import defaultdict

"""
    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Follow up:
    Could you do this in-place?
"""
def rotate_image(mtx):
    n = len(mtx)

    if n < 2:
        return

    for i in range(0, n / 2):
        for j in range(0, n):
            mtx[i][j], mtx[n - 1 - i][j] = mtx[n - 1 - i][j], mtx[i][j]

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]


def rotate_image2(mtx):
    n = len(mtx)

    if n < 2:
        return

    for i in range(0, (n + 1) / 2):
        for j in range(0, n / 2):
            tmp = mtx[i][j]
            mtx[i][j] = mtx[n - 1 - j][i]
            mtx[n - 1 - j][i] = mtx[n - 1 - i][n - 1 - j]
            mtx[n - 1 - i][n - 1 - j] = mtx[j][n - 1 - i]
            mtx[j][n - 1 - i] = tmp


mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_image(mtx)
for line in mtx:
    print line
