import sys
import os
import math
import imp
from collections import deque

"""
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (ie, buy one and sell one share
    of the stock), design an algorithm to find the maximum profit.
"""
def maxProfit(prices):
    max_profit = 0
    lowest_price = sys.maxint
    for i in range(0, len(prices)):
        lowest_price = min(lowest_price, prices[i])
        max_profit = max(max_profit, prices[i] - lowest_price)
    return max_profit

#prices = [1, 2, 3, 4, 5]
#print maxProfit(prices)
