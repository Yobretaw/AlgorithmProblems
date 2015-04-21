import sys
import math

"""
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
    which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container.
"""
def most_water(arr):
        n = len(arr)
        if n < 2:
            return 0

        start = 0
        end = n - 1

        max_water = 0
        while start < end:
            max_water = max((end - start) * min(arr[start], arr[end]), max_water)
            if arr[start] > arr[end]:
                end -= 1
            else:
                start += 1

        return max_water

