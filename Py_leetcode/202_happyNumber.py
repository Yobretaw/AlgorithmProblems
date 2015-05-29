import sys
import os
import re
import math
from collections import deque
from sets import Set

"""
    Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which 
    does not include 1. Those numbers for which this process ends in 1 are happy numbers.

    Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""
def is_happy(n):
    seen = set()
    while n != 1:
        s = [int(c) for c in str(n)]
        n = reduce(lambda x, y: x + y ** 2, s, 0)
        if n in seen:
            return False
        seen.add(n)

    return True

#print is_happy(29)
