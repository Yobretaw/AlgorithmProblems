import sys
import math

"""
    There are two sorted arrays A and B of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).
"""
def find_median_sorted_arrays(a, b):
    m = len(a)
    n = len(b)


def find_help(a, i, m, b, j, n, k):
    if k == 1:
        return min(a[i + 0], b[j + 0])

    if m == 1:
        return a[i]
    elif n == 1:
        return b[j]

    mid_a = a[i + m / 2]
    mid_b = a[j + n / 2]

    if mid_a > mid_b:
        if m / 2 + n / 2 + 1 >= k:
            return find_help(a, i, m - m / 2 - 1, b, j, n, k - m / 2  - 1)
        else:
            return find_help(a, i, m, b, j + n / 2, n - n / 2 - 1, k - n / 2 - 1)
    else:
        if m / 2 + n / 2 +1 >= k:
            return find_help(a, i, m, b, j, n - n / 2 - 1, k - n / 2 - 1)
        else:
            return find_help(a, i + m / 2, m - m / 2 - 1, b, j, n, k - m / 2 - 1)



a = [1, 2, 3]
b = [1, 2, 3]
print find_median_sorted_arrays(a, b)
