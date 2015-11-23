import sys
import math

"""
    Suppose you start at the top-left corner of an n x m matrix A and want to
    get to the bottom-right corner. The only way you can move is by either going
    right or going down.

    How many ways can you go from the top-left to bottom-right in an n x m matrix?
    How would you count the number of ways in the presence of obstacles, specified
    by an n x m boolean matrix, where True represents an obstacle.
"""
def compute_ways_without_obstacles(n, m):
    return factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1))

def factorial(m):
    res = 1
    while m >= 1:
        res *= m
        m -= 1
    return res

def compute_ways_with_obstacles(mtx):
    m, n = len(mtx), len(mtx[0])

    mem = [0] * m
    for i in range(m):
        if mtx[0][i]:
            break
        mem[i] = 1

    for i in range(1, n):
        for j in range(1, m):
            mem[j] = 0 if mtx[i][j] else (mem[j] + mem[j - 1])

    return mem[-1]


"""
    Variant 17.4.1

    A decimal number is a sequence of digits, i.e., a sequence over [0, 1, .., 9].
    The sequence has to be of length 1 or more, and the first element in the sequ-
    ence cannot be 0. Call a decimal number D monotone if D[i] <= D[i + 1], 0 <= i
    <= |D|. Write a function that takes as input a positive k, and computes the
    number of decimal numbers of length k that are monotone.
"""
def compute_number_monotone(k):
    return compute_ways_without_obstacles(k + 1, 9)


"""
    Variant 17.4.2

    Call a decimal number D 'strict monotone' if D[i] < D[i + 1], 0 <= i < |D|.
    Write a function which takes as input a positive integer k and computes the
    number of decimal numbers of length k that are strict monotone.
"""
def compute_number_strict_monotone(k):
    if k > 9:
        return 0
    
    return 10 - k

if __name__ == '__main__':
    print compute_ways_without_obstacles(3, 3)
    
    mtx = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print compute_ways_with_obstacles(mtx)
    print compute_number_monotone(2)
