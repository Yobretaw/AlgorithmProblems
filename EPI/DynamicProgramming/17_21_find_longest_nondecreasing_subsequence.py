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
        for j in range(i):
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


"""
    Variant 17.21.1

    Define a sequence of numbers <a_0, a_1, ..., a_{n-1}> to be alternating if
    a_i < a_{i + 1} for even i and a_i > a_{i + 1} for odd i. Given an array A
    of numbers with length n, find a longest subsequence <i_0, i_1, ..., i_{k-1}>
    such that <A[i_0], A[i_1], ..., A[i_{k - 1}]> is alternating.
"""
def longest_alternating_subsequence(A):
    n = len(A)

    # f[i] stores a tuple (a, b) where a represents the index of previous element
    # and b represents the length of the longest sequence that ends at i
    f = [(-1, 1)] * n

    for i in range(1, n):
        for j in range(i):
            l = f[j][1]
            if (l & 1 and A[i] > A[j] or not l & 1 and A[i] < A[j]) and f[i][1] < 1 + f[j][1]:
                f[i] = (j, 1 + f[j][1])
    return max(e[1] for e in f)

# In an alternating subsequence each point is a local extreme (i.e., either a
# local maximum or a local minimum). And we can easily verify that if we take
# a sequence and remove any element, the number of local extremes will not
# increase: if you remove some element "on a slope" that wasn't a local extreme,
# nothing changes, and if you remove a local extreme, you either lose it or it
# shifts to one of its two neighbors. (A slightly more careful formulation is
# needed for sequences with equal elements.)
# Hence, the best you can get is to take all the local extremes of the current sequence:

# This algorithm takes O(n) time
def longest_alternating_subsequence2(A):
    if A == []:
        return []

    res = []
    for a in A:
        if res and res[-1] == a:
            continue
        elif len(res) < 2:
            res.append(a)
            continue
        elif (a - res[-1]) * (res[-1] - res[-2]) < 0:
            res.append(a)
            continue
        else:
            res[-1] = a

    if res[0] > res[1]:
        res.pop(0)

    return len(res)


if __name__ == '__main__':
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    print find_longest_subsequence(A)
    print find_longest_subsequence2(A)
    #print sorted(A)

    #for i in range(100):
    #    A = [int(100 * random.random()) for i in xrange(1000)]
    #    print len(find_longest_subsequence(A)) == len(find_longest_subsequence2(A))

    print longest_alternating_subsequence(A)

    A = [0, 8, 9, 4, 1, 5, 6, 5, 9, 4]
    print longest_alternating_subsequence(A)
    print longest_alternating_subsequence2(A)

    A = [1, 2, 3, 4, 5]
    print longest_alternating_subsequence(A)
    print longest_alternating_subsequence2(A)

    for i in range(1000):
        A = [int(100 * random.random()) for j in xrange(200)]
        print i, longest_alternating_subsequence(A) == longest_alternating_subsequence2(A)
