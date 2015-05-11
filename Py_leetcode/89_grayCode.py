import sys
import os
import math

"""
    The gray code is a binary numeral system where two successive values differ in only one bit.

    Given a non-negative integer n representing the total number of bits in the code, print the sequence
    of gray code. A gray code sequence must begin with 0.

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2

    Note:
    For a given n, a gray code sequence is not uniquely defined.

    For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

    For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

    Refl :http://en.wikipedia.org/wiki/Gray_code
"""
def gray_code(n):
        if not n:
            return [0]

        res = [0] * (2 ** n)
        for i in range(0, n):
            offset = 2 ** i
            cycle_len = 2 ** (i + 1)
            is_one = True
            for j in range(offset, 2 ** n):
                if cycle_len <= 0:
                    cycle_len = 2 ** (i + 1)
                    is_one = not is_one

                if is_one:
                    res[j] |= 1 << i
                cycle_len -= 1
        return res


print gray_code(1)
