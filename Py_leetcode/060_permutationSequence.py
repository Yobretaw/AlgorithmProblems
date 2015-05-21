import sys
import os
import math

"""
    The set [1,2,3, ...,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order,
    We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

    Given n and k, return the kth permutation sequence.
    Note: Given n will be between 1 and 9 inclusive.
"""
def permutation_sequence(n, k):
    fac = [1]
    for i in range(1, n):
        fac.append(i * fac[-1])

    k -= 1
    nums = [0] * n
    res = []
    for i in range(0, n):
        d = k / fac[n - 1 - i]
        k %= fac[n - 1 - i]

        next_val = get_next_val(nums, d)
        res.append(next_val)

    return ''.join([str(c) for c in res])

def get_next_val(arr, k):
    count = 0
    last_idx = 0
    for i in range(0, len(arr)):
        if not arr[i]:
            if count == k:
                arr[i] = 1
                return i + 1
            else:
                last_idx = i
                count += 1
    return last_idx + 1


def permutation_sequence2(n, k):
    fac = [1]
    for i in range(1, 10):
        fac.append(i * fac[-1])

    res = ''
    nums = [str(i) for i in range(1, 10)]
    while n > 0:
        d = (k - 1) / fac[n - 1]
        res += nums[d]
        nums.remove(nums[d])
        k -= d * fac[n - 1]
        n -= 1
    return res

for i in range(0, math.factorial(4)):
    print permutation_sequence(4, i + 1)
    #print permutation_sequence2(4, i + 1)

