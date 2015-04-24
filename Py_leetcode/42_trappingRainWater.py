import sys
import math
from collections import defaultdict

"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

    For example, 
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
def trapping_water(a):
    if not a or len(a) == 1:
        return 0

    n = len(a)
    volume = 0
    left = 0
    right = n - 1
    max_left = 0
    max_right = 0
    while left < right:
        if a[left] > max_left:
            max_left = a[left]
        if a[right] > max_right:
            max_right = a[right]

        if a[left] > a[right]:
            volume += max_right - a[right]
            right -= 1
        else:
            volume += max_left - a[left]
            left += 1

    return volume

#a = [0,1,0,2,1,0,1,3,2,1,2,1]
#print trapping_water(a)
