import sys
import math

"""
    There are two sorted arrays A and B of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).
"""
def find_median_sorted_arrays(a, b):
    m = len(a)
    n = len(b)

    if (m + n) & 1:
        return find_help(a, 0, m, b, 0, n, (m + n)/2)
    else:
        return (find_help(a, 0, m, b, 0, n, (m + n)/2) + find_help(a, 0, m, b, 0, n, (m + n)/2 + 1))/2.0


def find_help(a, i, m, b, j, n, k):
    if m == 0 or n == 0:
        return a[i + k - 1] if n <= 0 else b[j + k - 1]

    if k <= 1:
        return min(a[i], b[j])

    mid_a = a[i + m/2]
    mid_b = b[j + n/2]

    if m/2 + n/2 + 1 >= k:
        if mid_a > mid_b:
            return find_help(a, i, m/2, b, j, n, k)
        else:
            return find_help(a, i, m, b, j, n/2, k)
    else:
        if mid_a > mid_b:
            return find_help(a, i, m, b, j + (n/2 + 1), n - (n/2 + 1), k - (n/2 + 1))
        else:
            return find_help(a, i + (m/2 + 1), m - (m/2 + 1), b, j, n, k - (m/2 + 1))


#a = [i for i in range(0, 100)]
#b = [i + 100 for i in a]

#print find_median_sorted_arrays(a, b)

#for i in range(0, len(a) + len(b)):
#    print i + 1, find_help(a, 0, len(a), b, 0, len(b), i + 1)
