import sys
import math

"""
    Divide two integers without using multiplication, division and mod operator.

    If it is overflow, return MAX_INT.
"""
INT_MAX = 2147483647
INT_MIN = -INT_MAX - 1

def divide(a, b):
    sign = 1 if a < 0 ^ b < 0 else 0

    if a < 0:
        a = ~a + 1
    if b < 0:
        b = ~b + 1

    if a < b:
        return 0

    if a == b:
        return 1 if not sign else -1

    res = 0
    while a >= b:
        m = 1
        while (m * b) << 1 < a:
            m <<= 1
        a -= m * b

        if not sign and res > INT_MAX - m:
            return INT_MAX
        elif sign and res > INT_MAX - m + 1:
            return INT_MIN

        res += m

    return res if not sign else ~res + 1


#print divide(10, 2)
#print divide(120, 20)
#print divide(-1, 1)
#print divide(5, 2)
#print divide(-1006986286, -2145851451)
