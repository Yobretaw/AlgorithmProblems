import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Implement a function which takes a 2D array A and prints A in spiral order
    ============================================================================================
"""
def spiralPrint(A):
    m = len(A)
    if m == 0:
        return

    n = len(A[0])
    if n == 0:
        return

    x_begin = 0
    x_end = n
    y_begin = 0
    y_end = m

    while True:
        if x_begin >= x_end:
            break

        for i in range(x_begin, x_end):
            print A[y_begin][i]

        y_begin += 1
        if y_begin >= y_end:
            break

        for i in range(y_begin, y_end):
            print A[i][x_end - 1]

        x_end -= 1
        if x_end <= x_begin:
            break

        for i in reversed(range(x_begin, x_end)):
            print A[y_end - 1][i]

        y_end -= 1
        if x_begin >= y_end:
            break

        for i in reversed(range(y_begin, y_end)):
            print A[i][x_begin]

        x_begin += 1

A = [
        [1]
    ]

B = [
        [1, 2],
        [3, 4]
    ]

C = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

D = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

#spiralPrint(A)
#print '-'*100

#spiralPrint(B)
#print '-'*100

#spiralPrint(C)
#print '-'*100

#spiralPrint(D)

"""
    Variant 6.22.1: Given a dimension d, write a program to generate a d x d 2D array which when printed
    in spiral order outputs the sequence [1, 2, 3,..., d^2]. For example, if d = 3, then the result should
    be 
                
                A = [
                    [1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]
                ]
"""
def generateSpiralMatrix(d):
    A = [[0 for i in range(0, d)] for i in range(0, d)]

    x_begin = 0
    x_end = d
    y_begin = 0
    y_end = d

    curr = 1
    while curr <= d ** 2:
        for i in range(x_begin, x_end):
            A[y_begin][i] = curr
            curr += 1

        if curr > d ** 2:
            break

        y_begin += 1
        for i in range(y_begin, y_end):
            A[i][x_end - 1] = curr
            curr += 1

        if curr > d ** 2:
            break

        x_end -= 1
        for i in reversed(range(x_begin, x_end)):
            A[y_end - 1][i] = curr
            curr += 1

        if curr > d ** 2:
            break

        y_end -= 1
        for i in reversed(range(y_begin, y_end)):
            A[i][x_begin] = curr
            curr += 1

        x_begin += 1

    return A

print generateSpiralMatrix(3)


"""
    Variant 6.22.2: Given a sequence of integers a, compute a 2D array A which when printed in spiral order
    yields a. (assume len(str(a)) = n^2 for some positive integer n)
"""
def generateMatrix(a):
    m = 1
    while m * 10 <= a:
        m *= 10

    d = int(math.sqrt(len(str(a))))
    A = [[0 for i in range(0, d)] for i in range(0, d)]

    x_begin = 0
    x_end = d
    y_begin = 0
    y_end = d

    curr = a / m
    while m > 0:
        for i in range(x_begin, x_end):
            A[y_begin][i] = curr

            a %= m
            m /= 10

            curr = a / m if m != 0 else 0

        if m == 0:
            break

        y_begin += 1
        for i in range(y_begin, y_end):
            A[i][x_end - 1] = curr

            a %= m
            m /= 10
            curr = a / m if m != 0 else 0

        if m == 0:
            break

        x_end -= 1
        for i in reversed(range(x_begin, x_end)):
            A[y_end - 1][i] = curr

            a %= m
            m /= 10
            curr = a / m if m != 0 else 0

        if m == 0:
            break

        y_end -= 1
        for i in reversed(range(y_begin, y_end)):
            A[i][x_begin] = curr

            a %= m
            m /= 10
            curr = a / m if m != 0 else 0

        x_begin += 1

    return A

print generateMatrix(123456789)
