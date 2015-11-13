import sys
import math


"""
    Design an efficient algorithm for computing 'n choose k', which has the
    property that it never overflows if 'n choose k' can be represented as a
    32-bit integer; assume n and k are integers.
"""
def compute_binomial_coefficient(n, k):
    if k >= n:
        return 0 if k > n else 1

    gcd = lambda m,n: m if not n else gcd(n,m%n)

    MAX_INT = 1 << 31

    start_val = k + 1
    accu_val = k + 1
    next_val = k + 2

    start_div = 1
    accu_div = 1
    next_div = 2

    reset_var = True

    while start_val < n or start_div < n - k:
        if start_val < n and accu_val <= MAX_INT / next_val:
            accu_val *= next_val
            reset_var = True
            start_val += 1
        elif start_div < n - k and accu_div <= MAX_INT / next_div:
            accu_div *= next_div
            next_div += 1
            start_div += 1
        else:
            d = gcd(accu_val, accu_div)
            if d > 1:
                accu_val /= d
                accu_div /= d
            else:
                d = gcd(next_val, accu_div)
                if d > 1:
                    accu_div /= d
                    next_val /= d
                    reset_var = False

        if reset_var:
            next_val = start_val + 1

    return accu_val / accu_div

def compute_binomial_coefficient2(n, k):
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
        print compute_binomial_coefficient2(30, i)
