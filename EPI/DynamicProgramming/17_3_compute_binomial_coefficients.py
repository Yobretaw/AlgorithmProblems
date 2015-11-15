import sys
import math


"""
    Design an efficient algorithm for computing 'n choose k', which has the
    property that it never overflows if 'n choose k' can be represented as a
    32-bit integer; assume n and k are integers.
"""
def compute_binomial_coefficient(n, k):
    """
        We can use the fact:

            (n choose k) = (n - 1 choose k) + (n - 1 choose k - 1)

        to build a table.
    """
    a = [0] * (k + 1)
    a[0] = 1
    for i in range(n + 1):
        for j in reversed(range(1, min(i, k) + 1)):
            a[j] += a[j - 1]
    return a[-1]


if __name__ == '__main__':
    for i in range(1, 21):
        print compute_binomial_coefficient(30, i)
