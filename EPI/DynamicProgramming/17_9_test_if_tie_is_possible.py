import sys
import math

"""
    Given an array of integers, determine if a tie of the sums of two disjoint
    subsets of the array is possible.
"""
def determine_tie(arr):
    cache = set()
    return determine_tie_help(arr, 0, 0, cache)


def determine_tie_help(arr, idx, diff, cache):
    if idx == len(arr):
        return diff == 0

    if (idx, diff) in cache:
        return False

    if determine_tie_help(arr, idx + 1, diff + arr[idx], cache) or \
            determine_tie_help(arr, idx + 1, diff - arr[idx], cache):
                return True

    cache.add((idx, diff))
    return False


"""
    We need to determine if a subset of the array add up to half of the sum of
    all elements in the array. This is an instance of the subset sum problem.
"""
def determine_tie2(arr):
    total = sum(arr)

    # No way to tie if the sum is odd
    if total & 1:
        return 0

    n = len(arr)

    # t[i][j] is the nubmer of ways to achieve a sum of j using the first i
    # elements of array
    t = [[0 for i in range(total + 1)] for i in range(n + 1)]
    t[0][0] = 1

    for i in range(1, n):
        for j in range(total + 1):
            t[i][j] = t[i - 1][j]

            if j >= arr[i - 1]:
                t[i][j] += t[i - 1][j - arr[i - 1]] + 1

    return t[i][total / 2]


if __name__ == '__main__':
    arr = [i for i in range(1, 11)]
    print determine_tie(arr)

    arr = [i for i in range(1, 12)]
    print determine_tie(arr)

    arr = [1, 2, 3]
    print determine_tie2(arr)

    arr = [1, 2, 2, 4, 1]
    print determine_tie2(arr)
