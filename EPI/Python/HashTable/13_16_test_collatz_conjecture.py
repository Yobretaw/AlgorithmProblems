import os
import math
import sys
from collections import defaultdict, Counter

"""
    The Collatz conjecture is the following: Take any natural number. If it's
    odd, triple it and add one; if it's even, halve it. Repeat the process
    indefinitely. No matter what number you begin with, you will eventually
    arrive at 1.

    Test the Collatz conjecture for the first n positive integers.
"""
def test_first_n_numbers(n):
    tested = set()
    for x in range(2, n + 1):
        y = x
        while x != 1:
            if x in tested:
                break

            if x % 2 == 0:
                x >>= 1
            else:
                x = 3 * x + 1
        tested.add(y)

    print len(tested)

test_first_n_numbers(10000)
