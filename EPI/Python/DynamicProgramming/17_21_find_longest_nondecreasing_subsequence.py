import sys
import math
import random

"""
    Given an array A of n numbers, find a longest subsequence 

                    <i_0, i_1, ..., i_{k - 1}>

    such that i_j < i_{j + 1} and A[i_j] < A[i_{j + 1}] for any j in [0, k - 2]
"""
def longest_nondecreasing_subsequence(A):
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
def longest_nondecreasing_subsequence2(A):
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


"""
    Variant 17.21.3

    Define a sequence of numbers <a_0, a_1, ..., a_n> to be convex if a_i < 
    (a_{i-1} + a_{i+1}) / 2, for 1 <= i <= n - 2. Given an array of numbers
    A of length n, find a longest subsequence <i_0, i_1, ..., i_{k-1}> such
    that <A[i_0], A[i_1], ..., A[i_{k-1}]> is convex.
"""
def longest_convex_subsequence(A):
    n = len(A)

    # f[i] = (a, b) where a is the index of previous element the sequence
    # and b is the length of the subsequence ending at A[i]
    f = [(-1, 0) for i in range(n)]
    f[0] = (-1, 0)
    f[1] = (0, 0)

    for i in range(2, n):
        for j in range(1, i):
            if (A[i] + A[f[j][0]]) / 2 > A[j]:
                f[i] = (j, 1 + f[j][1])

    return max(e[1] for e in f)


"""
    Variant 17.21.4

    Defind a sequence of numbers <a_0, a_1, ..., a_{n-1}> to be bitonic if
    there exists k such that a_i < a_{i+1} for 0 <= i < k, and a_i > a_{i+1}
    for k <= i < n - 1. Given an array of numbers A of length n, find a longest
    subsequence <i_0, i_1, ..., i_{k-1}> such that <A[i_0], A[i_1], ..., A[i_{k-1}]>
    is bitonic.
"""
def longest_bitonic_subsequence(A):
    n = len(A)
    
    # f[i] = [(a, b), (c, d)] where (a, b) represents info of the increasing part,
    # while (c, d) stores info of the decreasing part.
    f = [[(-1, 0), (-1, 0)] for i in range(n)]
    f[0] = [(-1, 1), (-1, 1)]

    for i in range(1, n):
        for j in range(i):
            # keep increasing
            if A[i] > A[j] and f[i][0][1] < 1 + f[j][0][1]:
                f[i][0] = (j, 1 + f[j][0][1])

            # start/continue decreasing
            if A[i] < A[j] and f[i][1][1] < 1 + max(f[j][0][1], f[j][1][1]):
                f[i][1] = (j, 1 + max(f[j][0][1], f[j][1][1]))

    return max(e[1][1] for e in f)


# Another approach which takes O(nlogn) time is to use the idea of longest
# increasing subsequence(LIS). We find the LIS of the input A and the reverse
# of A, and then traverse both results to get the longest bitonic subsequence.



"""
    Variant 17.21.5

    Define a sequence of points in the plane to be ascending if each point is
    above and to the right of the previous point. How would you find a maximum
    ascending subset of a set of points in the plane?

    ----

    The idea is to first sort all points by their x coordinates. Then we find
    the longest increasing subsequence of the list of the y coordinates of
    the sorted points
"""

if __name__ == '__main__':
    #A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    #print longest_nondecreasing_subsequence(A)
    #print longest_nondecreasing_subsequence2(A)

    #print longest_alternating_subsequence(A)

    #A = [0, 8, 9, 4, 1, 5, 6, 5, 9, 4]
    #print longest_alternating_subsequence(A)
    #print longest_alternating_subsequence2(A)

    #A = [1, 2, 3, 4, 5]
    #print longest_alternating_subsequence(A)
    #print longest_alternating_subsequence2(A)

    #for i in range(1000):
    #    A = [int(100 * random.random()) for j in xrange(200)]
    #    print i, longest_alternating_subsequence(A) == longest_alternating_subsequence2(A)

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    print longest_convex_subsequence(A)

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    print longest_bitonic_subsequence(A)

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print longest_bitonic_subsequence(A)

    A = [12, 4, 78, 90, 45, 23]
    print longest_bitonic_subsequence(A)
