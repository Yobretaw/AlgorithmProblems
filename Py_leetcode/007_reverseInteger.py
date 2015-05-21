import sys
import math

"""
    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

    -   If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

    -   Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
        then the reverse of 1000000003 overflows. How should you handle such cases?

    -   For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
def reverseInteger(x):
        if -10 < x < 10:
            return x

        sign = -1 if x < 0 else 1
        x = max(x, -x)

        while x % 10 == 0:
            x /= 10

        d = 10
        res = 0
        while x > 0:
            # check overflow
            if res > (sys.maxint - x % d) / 10:
                return 0

            res *= 10
            res += x % d

            x /= 10

        return sign * res


#m = sys.maxint
#print m
#print reverseInteger(-123)
#print reverseInteger(int(str(sys.maxint)[::-1]))
#print reverseInteger(int(str(sys.maxint + 1)[::-1]))
