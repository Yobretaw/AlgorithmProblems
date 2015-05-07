import sys
import os
import math

"""
    Given a non-negative number represented as an array of digits, plus one to the number.

    The digits are stored such that the most significant digit is at the head of the list.
"""
def plus_one(digits):
    n = len(digits)
    digits[-1] += 1
    for i in reversed(range(0, n)):
        if digits[i] >= 10:
            digits[i] %= 10
            if i > 0:
                digits[i - 1] += 1
            else:
                digits.insert(0, 1)
    return digits
