import sys
import os
import math
import imp
from collections import deque

"""
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    Note:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    if n == 2:
        return max(0, prices[1] - prices[0])

    a = [0] * n
    lowest_price = prices[0]
    for i in range(1, n):
        lowest_price = min(lowest_price, prices[i])
        a[i] = max(a[i - 1], prices[i] - lowest_price)

    b = [0] * n
    highest_price = prices[n - 1]
    for i in reversed(range(0, n - 1)):
        highest_price = max(highest_price, prices[i])
        b[i] = max(b[i + 1], highest_price - prices[i])

    max_profit = 0
    for i in range(0, n):
        max_profit = max(max_profit, a[i] + b[i])
    
    return max_profit
