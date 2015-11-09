import sys
import os
import math
from copy import deepcopy


"""
    The gray code is a binary numeral system where two successive values differ
    in only one bit.

    Given a non-negative integer n representing the total number of bits in the
    code, print the sequence of gray code. A gray code sequence must begin with 0.

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

        00 - 0
        01 - 1
        11 - 3
        10 - 2

    Note:
    For a given n, a gray code sequence is not uniquely defined.

    For example, [0,2,3,1] is also a valid gray code sequence according to the
    above definition.
"""
def compute_gray_code2(n):
        seq = [0]
        count = 0
        while count < n:
            seq.extend([(num | 1 << count) for num in seq[::-1]])
            count += 1

        return seq[:n]


if __name__ == '__main__':
    for l in compute_gray_code2(0):
        print l
