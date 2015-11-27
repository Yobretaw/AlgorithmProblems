import sys
import math


"""
    There are N gas stations along a circular route, where the amount of gas at
    station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
    from station i to its next station (i+1). You begin the journey with an empty
    tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit
    once, otherwise return -1.

    Note:
    The solution is guaranteed to be unique.
"""
def find_start_station(gas, cost):
        n = len(gas)

        gas_remaining = 0
        gas_sum = 0
        start = 0
        for i in range(n):
            gas_remaining += gas[i] - cost[i]
            gas_sum += gas[i] - cost[i]

            # not enough gas to reach station[i]. Set next station as the new
            # starting station
            if gas_remaining < 0:
                start = i + 1
                gas_remaining = 0

        return start if gas_sum >= 0 else -1

if __name__ == '__main__':
    gas = [2, 4]
    cost = [3, 4]
    print find_start_station(gas, cost)

    gas = [1, 2]
    cost = [2, 1]
    print find_start_station(gas, cost)
