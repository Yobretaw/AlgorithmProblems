import sys
import os
import math

"""
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    Note:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to
    hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
def merge_array(a, m, b, n):
        if not m:
            a[:n] = b[:]
            return
        elif not n:
            return

        end = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            a_val = a[m] if m >= 0 else -sys.maxint
            b_val = b[n] if n >= 0 else -sys.maxint
            print a_val, b_val
            if a_val > b_val:
                a[end] = a_val
                m -= 1
            else:
                a[end] = b_val
                n -= 1
            end -= 1
        return

a = [1, 0]
m = 1
b = [2]
n = 1

merge_array(a, m, b, n)
print a
