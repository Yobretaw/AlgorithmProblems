import sys
import math
from collections import defaultdict

"""
    There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
"""
def candy(ratings):
    n = len(ratings)
    if n < 2:
        return n
    
    inc = 1
    counts = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            inc += 1
            counts[i] = inc
        else:
            inc = 1

    inc = 1
    for i in reversed(range(0, n - 1)):
        if ratings[i] > ratings[i + 1]:
            inc += 1
            counts[i] = max(counts[i], inc)
        else:
            inc = 1

    return sum(counts)

#ratings = [1, 2, 3, 1, 3, 1]
#print candy(ratings)
