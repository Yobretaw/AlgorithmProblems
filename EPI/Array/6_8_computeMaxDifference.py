import sys
import os
import re
import math
import random

"""
    ============================================================================================
    A robot needs to travel along a path that includes serveral ascents and descents. When it
    goes up, it uses battery to power the motor and when it descends, it recovers the energy
    which is stored in battery. The battery recharging process is ideal: on descending, every
    Joule of gravitational potential energy converts t oa Joule of electrical energy which is
    stored in the battery. The battery has a limited capacity and once it reaches this capacity,
    the energy generated in descending is lost.

    Design an algorithm that takes a sequence of n three-dimensional coordinates to be traversed,
    and returns the minimum battery capacity needed to complete the journey. The robot begins
    with the battery fullly charged.
    ============================================================================================
"""
def minimum_battery_capacity(heights):
    if len(heights) == 0:
        return 0

    max_diff = -sys.maxint  # initial height
    curr_diff = max_diff
    for i in range(1, len(heights)):
        curr_diff += heights[i] - heights[i - 1]

        if curr_diff < 0:
            curr_diff = 0
        elif curr_diff > max_diff:
            max_diff = curr_diff

    return max_diff

def minimum_battery_capacity2(heights):
    if len(heights) == 0:
        return 0

    min_height = sys.maxint
    capacity = 0
    for height in heights:
        capacity = max(capacity, height - min_height)
        min_height = min(height, min_height)

    return capacity


#l = [random.randint(1, 1000) for i in range(0, 100)]
#print min(l), max(l)
#print minimum_battery_capacity(l)
#print minimum_battery_capacity2(l)
#print minimum_battery_capacity(l) == minimum_battery_capacity2(l)


"""
    ============================================================================================
    Variant 6.8.1: Let A be an array of integers. Find the length of a longest subarray all of 
    whose entries are equal.
    ============================================================================================
"""
def find_longest_subarray(A):
    n = len(A)

    if n < 2:
        return n

    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if A[i] == A[i - 1]:
            curr_len += 1

            if curr_len > max_len:
                max_len = curr_len
        else:
            curr_len = 1

    return max_len

#print find_longest_subarray([1, 2, 2, 4, 3, 3, 3, 4, 4, 4, 4, 3, 2, 1, 1, 1])
