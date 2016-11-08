import sys
import math

"""
    Given an circular array A, computes its maximum subarray sum in O(n) time,
    where n is the length of A. Can you devise an algorithm that takes O(n)
    time and O(1) space.
"""
def compute_max_subarray_sum(arr):
    n = len(arr)
    if n < 2:
        return 0 if not n else max(0, arr[0])

    # first check if all elements are negative
    i = 0
    while i < n:
        if arr[i] > 0:
            break
        i += 1

    # if all elements are negative, return 0
    if i == n:
        return 0

    # find the maximum postfix sum and the corresponding starting index
    # of that postfix
    postfix_sum = postfix_max = 0
    idx = n
    for i in reversed(range(n)):
        postfix_sum += arr[i]
        if postfix_sum > postfix_max:
            postfix_max = postfix_sum
            idx = i

    prefix_sum = prefix_max = 0
    global_max = prefix_max + postfix_max
    for i in range(n):
        val = arr[i]

        prefix_sum += val
        prefix_max = max(prefix_max, prefix_sum)

        if i >= idx:
            postfix_max -= val

        global_max = max(global_max, prefix_max + postfix_max)

    return global_max


if __name__ == '__main__':
    arr = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    print compute_max_subarray_sum(arr)

    arr = [904, 40, 523, 12, 481]
    print compute_max_subarray_sum(arr)

    arr = [8, -8, 9, -9, 10, -11, 12]
    print compute_max_subarray_sum(arr)

    arr = [10, -3, -4, 7, 6, 5, -4, -1]
    print compute_max_subarray_sum(arr)

    arr = [-1, 40, -14, 7, 6, 5, -4, -1]
    print compute_max_subarray_sum(arr)
