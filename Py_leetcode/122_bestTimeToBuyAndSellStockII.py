import sys
import os
import math
import imp
from collections import deque

"""
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as
    you like (ie, buy one and sell one share of the stock multiple times). However, you may not
    engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit += max(0, prices[i] - prices[i - 1])
    return max_profit


#prices = [1, 2]
#prices = [2,1,2,0,1]
#prices = [3,3,5,0,0,3,1,4]
#print maxProfit(prices)
