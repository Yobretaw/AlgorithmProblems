import sys
import math
import random

"""
    Given an array A of n numbers, find a longest subsequence 

                    <i_0, i_1, ..., i_{k - 1}>

    such that i_j < i_{j + 1} and A[i_j] < A[i_{j + 1}] for any j in [0, k - 2]
"""
def find_longest_subsequence(A):
    n = len(A)

    # f[i] stores a tuple (a, b) where a is the index of previous element that
    # yields the longest subsequence, and b is the length of the longest
    # subsequence ends at A[i]
    f = [[-1, 1]] * n

    for i in range(1, n):
        for j in range(0, i):
            if A[i] >= A[j] and f[i][1] < 1 + f[j][1]:
                f[i] = (j, 1 + f[j][1])


    max_len = max(e[1] for e in f)

    for i in range(max_len, n):
        if f[i][1] == max_len:
            idx = i
            curr = []
            while idx >= 0:
                curr.append(A[idx])
                idx = f[idx][0]
            return curr[::-1]
    return []

# O(nlogn) time
def find_longest_subsequence2(A):
    tail_values = []
    for v in A:
        idx = upper_bound(tail_values, v)
        if idx == len(tail_values):
            tail_values.append(v)
        else:
            tail_values[idx] = v
    return tail_values

# Return the index of the first element in input array A which does not compare
# greater than the given value v.
def upper_bound(A, v):
    n = len(A)
    if not n:
        return 0

    start = 0
    end = n
    while start < end:
        mid = start + (end - start) / 2
        if A[mid] <= v:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == '__main__':
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    print find_longest_subsequence(A)
    print find_longest_subsequence2(A)
    print sorted(A)

    for i in range(100):
        A = [int(100 * random.random()) for i in xrange(1000)]
        print len(find_longest_subsequence(A)) == len(find_longest_subsequence2(A))
