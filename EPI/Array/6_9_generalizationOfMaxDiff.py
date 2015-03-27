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
