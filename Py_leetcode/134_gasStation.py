import sys
import math
from collections import defaultdict

"""
    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i
    to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

    Note:
    The solution is guaranteed to be unique.
"""
def gas_station(cost, gas):
    n = len(cost)
    if n == 1:
        return 0 if gas[0] >= cost[0] else -1

    gas_need = 0
    gas_sum = 0
    start = 0
    for i in range(0, n):
        gas_remain += gas[i] - cost[i]
        gas_sum += gas[i] - cost[i]

        if gas_remain < 0:
            start = i + 1
            gas_remain = 0

    return start if gas_sum >= 0 else -1
