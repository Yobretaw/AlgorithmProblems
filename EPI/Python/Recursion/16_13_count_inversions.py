import sys
import os
import math


"""
    Let A be an array of n numbers. The pair of indices (i, j) is said to be
    inverted if i < j and A[i] > A[j].

    Design an efficient algorithm that takes an array A of n numbers and returns
    the number of inverted pairs of indices.
"""
def count_inversions(A):
    return count_inversions_help(A)[0]


def count_inversions_help(A):
    n = len(A)
    if n < 2:
        return 0, A

    left_count, left = count_inversions_help(A[:n/2])
    right_count, right = count_inversions_help(A[n/2:])

    left_idx = right_idx = 0
    total = 0
    while left_idx < len(left):
        if right_idx >= len(right):
            break

        while right_idx < len(right) and left[left_idx] > right[right_idx]:
            right_idx += 1
        
        total += right_idx
        left_idx += 1

    if left_idx < len(left):
        total += right_idx * (len(left) - left_idx)

    left_idx = right_idx = 0
    res = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1

    res.extend(left[left_idx:] if left_idx < len(left) else right[right_idx:])
    return left_count + right_count + total, res


if __name__ == '__main__':
    A = [4, 2, 6, 3, 1, 0]
    print count_inversions(A)

    A = [5, 4, 3, 2, 1]
    print count_inversions(A)
