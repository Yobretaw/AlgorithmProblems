import sys
import math
import imp
from collections import defaultdict

"""
    ...
"""
def get_skyline(buildings):
    if not buildings:
        return []

    n = len(buildings)
    for i in range(0, n - 1):
        curr = buildings[i]
        for j in range(i + 1, n):
            if buildings[j][0] < curr[1] and buildings[j][2] < curr[2]:
                buildings[j][0] = curr[1]
            elif buildings[j][0] >= curr[1]:
                break
    
    for i in reversed(range(1, n)):
        curr = buildings[i]
        for j in reversed(range(0, i)):
            if buildings[j][1] > curr[0] and buildings[j][2] < curr[2]:
                buildings[j][1] = curr[0]
            elif buildings[j][1] <= curr[0]:
                break

    print buildings
    #res = []
    #for i in range(0, n):
    #    res.append([buildings[i][0], buildings[i][2]])

print get_skyline([[2,9,10], [3,7,15], [5,8,12], [15,20,10], [19,24,8]])
