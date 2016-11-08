import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Write a function which takes as input a nonnegative integer n and returns the first n rows
    of Pascal's traingle.
    ============================================================================================
"""
def generateNthRowOfPascalTraingle(n):
    row = [1]
    result = [[1]]

    for i in range(1, n):
        for j in reversed(range(1, i)):
            row[j] = row[j - 1] + row[j]

        row.append(1)
        result.append(list(row))

    return result

#print generateNthRowOfPascalTraingle(1)
#print generateNthRowOfPascalTraingle(2)
#print generateNthRowOfPascalTraingle(3)
#print generateNthRowOfPascalTraingle(4)
print generateNthRowOfPascalTraingle(5)
