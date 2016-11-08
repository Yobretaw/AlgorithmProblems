import sys
import math
import random


"""
    Let A be an n x m Boolean 2D array. Design efficient algorithms for the
    following two problems.
    
        - What is the largest 2D subarray containing only 1s?
        - What is the largest square 2D subarray containing only 1s?

    What are the time and space complexities of the algorithms as a function
    of m and n.
"""
def largest_2d_subarray(mtx):
    m, n = len(mtx), len(mtx[0]) if mtx else 0
    if not m or not n:
        return 0
    
    H = [0] * n
    L = [0] * n
    R = [n - 1] * n

    ret = 0
    for i in range(0, m):
        left, right = 0, n - 1
        for j in range(0, n):
            if mtx[i][j]:
                H[j] += 1
                L[j] = max(L[j], left)
            else:
                left = j + 1
                H[j] = 0
                L[j] = 0

        for j in reversed(range(0, n)):
            if mtx[i][j]:
                R[j] = min(R[j], right)
                ret = max(ret, H[j] * (R[j] - L[j] + 1))
            else:
                right = j - 1
                R[j] = n - 1
    return ret


def largest_square(mtx):
    m, n = len(mtx), len(mtx[0]) if mtx else 0
    if not m or not n:
        return 0
    
    H = [0] * n
    L = [0] * n
    R = [n - 1] * n

    ret = 0
    for i in range(0, m):
        left, right = 0, n - 1
        for j in range(0, n):
            if mtx[i][j]:
                H[j] += 1
                L[j] = max(L[j], left)
            else:
                left = j + 1
                H[j] = 0
                L[j] = 0

        for j in reversed(range(0, n)):
            if mtx[i][j]:
                R[j] = min(R[j], right)
                ret = max(ret, min(H[j], (R[j] - L[j] + 1)) ** 2)
            else:
                right = j - 1
                R[j] = n - 1
    return ret
        

if __name__ == '__main__':
    mtx = [
        [1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    print largest_2d_subarray(mtx)
    print largest_square(mtx)

    mtx = [
        [1, 1]
    ]
    print largest_2d_subarray(mtx)
    print largest_square(mtx)
