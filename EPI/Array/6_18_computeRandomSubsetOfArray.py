import sys
import os
import re
import math
import random


"""
    ============================================================================================
    Design an algorithm that computes an array of size k consisting of distinct integers in the
    set {0, 1,..., n - 1}. All subsets should be equally likely and, in addition, all permutations
    of elements of the array should be equally likely. Your time complexity should be O(k). Your
    algorithm can use O(k) in addition to the k element array for the result. You may assume the
    existence of a library function which takes as input a nonnegative integer t and returns an
    integer in the set [0, 1,..., t - 1] with uniformlly probability.
    ============================================================================================

    Solution: We mimic the offline sampling algorithm described in Solution 6.16, with A[i] = i
    initially.

    The key to getting away with O(k) space is recognizing that most of the entries of A are
    unchanged when k << n. Therefore we simulate A with a hash table.

    Specifically, we maintain a hash table H whose keys and values are from {0, 1,..., n - 1}.
    Conceptually, H tracks indices of the array for which A[i] may not equal i. If i is a key
    in H, then the value in H corresponding to i is the value stored at A[i]. If H does not
    contain a key i, it means A[i] is still i.

    Initially H is empty. We do k iterations of the following. Choose a random integer r from
    [0, n - 1 - i], where i is the current iteration count, starting at 0. There are four
    possibilities, corresponding to whether or not the entries in A that are being swapped
    are already present in H. The desired result is in A[n - k, n - 1], which can be determined
    from H.
"""
def computeRandomSubset(n, k):
    H = {}

    for i in range(0, k):
        r = random.randint(0, n - 1 - i)

        val1 = H.get(r)
        val2 = H.get(n - 1 - i)

        if not val1 and not val2:
            H[r] = n - 1 - i
            H[n - 1 - i] = r
        elif not val1 and val2:
            H[r] = val2
            H[n - 1 - i] = r
        elif val1 and not val2:
            H[n - 1 - i] = val1
            H[r] = n - 1 - i
        else:
            H[r], H[n - 1 - i] = H[n - 1 - i], H[r]

    res = []
    for i in range(0, k):
        res.append(H[n - 1 - i])

    return res


count = [0] * 10
for i in range(0, 1000):
    res = computeRandomSubset(10, 5)
    for val in res:
        count[val] += 1
    print res

print count
