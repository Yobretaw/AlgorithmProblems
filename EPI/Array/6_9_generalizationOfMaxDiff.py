import sys
import os
import re
import math

"""
    ============================================================================================
                                    Max Profit Problem
    

    1. What's the maximum profit that can be made by buying and selling a share two times over
    a given day range?

    2. What's the maximum profit that can be made by buying and selling a share k times over
    a given day range? Here k is a fixed input parameter

    3. What's the maximum profit that can be made by buying and selling a share any times over
    a given day range?
    ============================================================================================
"""
def maxProfix1(prices):
    """
        We can solve this problem in O(n). We perform a forward interation and storing the best
        solution for prices[0:j], j between 1 and n - 1, inclusive. We then do a reverse interation,
        computing the best solution for prices[j:n - 1], j between 0 and n - 2, inclusive, which we
        combine with the result from the forward interation. The additional space complexity is
        O(n), which is the space used to store the best solutions for the subarrays.
    """
    n = len(prices)
        
    if n < 2:
        return 0

    forward = [0] * n
    min_val = prices[0]
    for i in range(1, n):
        if prices[i] < min_val:
            min_val = prices[i]

        if prices[i] - min_val > forward[i - 1]:
            forward[i] = prices[i] - min_val
        else:
            forward[i] = forward[i - 1]

    backward = [0] * n
    max_val = prices[n - 1]
    for i in reversed(range(0, n - 1)):
        if prices[i] > max_val:
            max_val = prices[i]

        if max_val - prices[i] > backward[i + 1]:
            backward[i] = max_val - prices[i]
        else:
            backward[i] = backward[i + 1]

    max_profit = 0
    for i in range(0, n):
        if forward[i] + backward[i] > max_profit:
            max_profit =forward[i] + backward[i]

    return max_profit


def maxProfix2(prices, k):
    """
        Formally , this problem is to compute the maximum valud of (A[j_0] - A[i_0]) + (A[j_1] - A[i_1])
        + ... + (A[j_k-1] - A[i_k-1]) subject to i_0 < j_0 < i_1 < j_1 < .. < i_k-1 < j_k-1.

        A straightforward algorithm is to interate over j from 1 to k and interate through A, recording
        for each index i the best solution for A[0:i] with j pairs. We store these solutions in an
        auxiliary array of length n. The overall time complexity will be O(kn^2); by reusing the arrays
        we can reduct to additional space complexity to O(n).

        We can improve the time complexity to O(kn), and the additional space complexity to O(k) as follows.
        Defind B(i, j) to be the most money you can have if you must make j - 1 buy-sell transaction prior
        to i-th day and buy at i-th day. Defind S(i, j) to tbe the maximum profit achievable with j buys
        and sells with the j-th sell taking place at i-th day. Then the following mutual recurrence holds:
                
                    S(i, j) = A[i] + max_{i' < i}(B(i, j))
                    B(i, j) = max_{i' < i}(S(i', j - 1)) - A[i]

        The key to achieving an O(kn) time bound is the observation that computing B and S requires computing
        max_{i' < i}(B(i', j - 1)) and max_{i' < i}(S(i', j - 1)). These two quantities can be computed in
        constant time for each i and j with a conditional update.
    """
    n = len(prices)
    
    if n < 2 or k < 1:
        return 0

    if k > n / 2:
        return maxProfix3(prices)

    k_sum = [-sys.maxint] * (2 * k)
    for i in range(0, n):
        j = 0
        sign = -1
        pre_k_sum = list(k_sum)

        while j < len(k_sum) and j <= i:
            diff = sign * prices[i] + (pre_k_sum[j - 1] if j != 0 else 0)
            k_sum[j] = max(diff, pre_k_sum[j])

            j += 1
            sign *= -1

    print k_sum
    return k_sum[-1]


def maxProfix3(prices):
    n = len(prices)
    profit = 0

    if n < 2:
        return 0

    for i in range(1, n):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            profit += diff

    return profit


print maxProfix2([1, 3], 0)
print maxProfix2([1, 2], 1)
print maxProfix2([2, 1], 0)
print maxProfix2([2, 1, 2, 0, 1], 2)
