import sys
import math
from collections import defaultdict

"""
    cost[i], gas[i]
"""
def gas_station(cost, gas):
    n = len(cost)
    if n == 1:
        return True if gas[0] >= cost[0] else False

    gas_need = 0
    gas_sum = 0
    start = 0
    for i in range(0, n):
        gas_remain += gas[i] - cost[i]
        gas_sum += gas[i] - cost[i]

        if gas_remain < 0:
            start = i
            gas_remain = 0

    return (start + 1) if gas_sum >= 0 else -1
