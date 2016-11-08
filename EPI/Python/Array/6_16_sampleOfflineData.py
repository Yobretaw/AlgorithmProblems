import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Let A be an array whose entries are all distinct. Implement an algorithm that takes A and an
    integer k and returns a subset of k elements of A. All subsets should be equally likely. Use
    as few calls to the random number generator as possible(which returns random integers) and 
    use O(1) additional space. You can return result in the same array as input.
    ============================================================================================

    Solution:
    
    The key to solve this problem is to build larger random subsets out of smaller ones

    The problem is trivial when k = 1. Let n be the length of A. We make one call to the
    random number generator, take the returned value mod n(call it r), and swap A[n - 1]
    with A[r]. The entry A[n - 1] holds the result.

    For k > 1, we begin by choosing one element at random as above and we now repeat the
    same process with the n - 1 elements subarray A[0:n-2]. Eventually, the random subset
    occupies the slots A[n-k:n-1] and the remaining elements are in the first n - k slots.

    The algorithm runs clearly in additional O(1) space. The correctness(i.e randomness)of
    this algorithm can be proved using mathematical induction.: if all subsets of size k
    are equally likely, then the construction process ensures that the subsets of size k + 1
    are also equally likely.

    The algorithm make k calls to the random number generator. When k is bigger than n/2,
    we can optimize by computing a subset of n - k elements to remove from the set. For
    example, when k = n - 1, this replaces n - 1 calls to the random number generator with
    a single call.
    
"""
def generateSubsets(A, k):
    n = len(A);

    if n < 2:
        return

    """
    The last k slots in A will be used to store the random set
    """
    for i in range(0, min(k, n - k)):
        next_pos = random.randint(0, n - i - 1)
        A[n - i - 1], A[next_pos] = A[next_pos], A[n - i - 1]

    if k > n / 2:
        A[:] = A[::-1]


#for i in range(0, 100):
#    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    generateSubsets(l, 8)
#    print l
