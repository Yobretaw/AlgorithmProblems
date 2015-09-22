import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function which takes as input an array and finds the distance between
    a closest pair of equal entries.
"""
def find_nearest_repeated_entries(arr):
    n = len(arr)
    if n < 2:
        return -1

    pos = {}
    dist = {}
    for i, v in enumerate(arr):
        if v in pos:
            d = i - pos[v] - 1
            if v in dist and d < dist[v]:
                dist[v] = d
            elif not v in dist:
                dist[v] = d
        pos[v] = i
    
    min_key, min_val = None, sys.maxint
    for k, v in dist.iteritems():
        if v < min_val:
            min_key = k
            min_val = v

    return min_key


#s = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
#print find_nearest_repeated_entries(s)
