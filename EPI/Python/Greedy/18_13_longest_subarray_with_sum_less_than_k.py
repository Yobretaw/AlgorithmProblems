import sys
import math

"""
    Design an algorithm that takes as input an array A of n numbers and a key k,
    and returns a longest subarray of A for which the subarray is less than k.
"""
def longest_subarray(A, k):
    if not A:
        return 0

    n = len(A)

    prefix_sum = [A[0]]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    # early return if the sum of A is less than k
    if prefix_sum[-1] < k:
        return 0, n - 1

    # build the min_prefix_sum where min_prefix_sum[i] is minimum possible sum
    # of a subarray that starts at 0 and extends to b or beyond.
    min_prefix_sum = [None] * n
    min_prefix_sum[-1] = prefix_sum[-1]
    for i in reversed(range(0, n - 1)):
        min_prefix_sum[i] = min(min_prefix_sum[i + 1], prefix_sum[i])

    """
        Let a <= b be the indices of elements in A. Define M(a, b) to be the
        minimum possible sum of a subarray beginning at a and extending to b
        or beyond. Note that M(0, b) = min_prefix_sum[b], and M(a, b) = 
        min_prefix_sum[b] - prefix_sum[a - 1], when a > 0. If M(a, b) > k, no
        subarray starting at a that includes b can satisfy the sum constraint,
        so we can increment a. If M(a, b) <= k, then we are assured that there
        exists a subarray of length b - a + 1 satisfying the sum constraint, so
        we compare the length of the longest subarray satisfying the sum constraint
        identified so far to b - a + 1 and conditionally update it. Consequently,
        we can increment b.

        Suppose we initialize a and b to 0 and iteratively perform the increments
        to a and b described above until b = n, then we will discover the length
        of the longest subarray that satisfies the sum constraint. We prove the
        correctness as follows.

        Let A[a* : b*] be the maximum length subarray that satisfies the sum
        constraint. Note that when we increment a to a + 1, A[a:b-1] does satisfy
        the sum constraint, but A[a:b] does not. This implies A[a:b-1] is the
        longest subarray starting at a that satisfies the sum constant.

        The iteration ends when b = n. At this point, we claim a >= a*. If not,
        then A[a:n - 1] satisfies the sum constraint, since we incremented b to
        n, and (n - 1) - a + 1 > b* - a* + 1, contracting the Optimality of
        A[a* : b*]. Therefore a must be assigned to a* at some iteration. At this
        point, b <= b* since A[a* - 1 : b* - 1] satisfies the sum constraint. If
        b > b*, then (b - 1) - (a* - 1) + 1 = b - a* + 1 > b* - a* + 1, violating
        the Optimality of A[a* : b*]. Since b <= b* and a = a*, the algorithm will
        increment b till it reaches b* (since A[a*:b*] satifies the sum constraint),
        and thus will identify b* - a* + 1 as the optimal solution.
    """
    a = b = 0
    max_length = 0
    res = None
    while a < n and b < n:
        min_curr_sum = (min_prefix_sum[b] - prefix_sum[a - 1]) if a > 0 else min_prefix_sum[b]

        if min_curr_sum <= k:
            curr_length = b - a + 1
            if curr_length > max_length:
                max_length = curr_length
                res = (a, b)
            b += 1
        else:
            a += 1

    return res
