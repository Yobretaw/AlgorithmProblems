import math


"""
    Given an integer n, count the total number of digit 1 appearing in all
    non-negative integers less than or equal to n.

    For example:
    Given n = 13,
    Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
def count_digit_one(n):
    if n < 1:
        return 0

    d = 1
    count = 0
    range_total = 0   # number of 1's in [0, d]
    while d <= n:
        r = n % d
        c = (n % (10 * d)) / d

        if c > 0:
            count = c * range_total + count + (d if c > 1 else (r + 1))

        range_total = 10 * range_total + d
        d *= 10

    return count


if __name__ == '__main__':
    for i in range(1, 100):
        print i, count_digit_one(i)
