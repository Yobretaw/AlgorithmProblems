import sys
import os
import math

"""
    Given n non-negative integers representing the histogram's bar height where the width
    of each bar is 1, find the area of largest rectangle in the histogram.

    For example, given height = [2,1,5,6,2,3], return 10.
"""
def largest_rectangle(height):
    n = len(height)
    if n < 2:
        return height[0] if n else 0

    height.append(0)
    max_area = 0
    for i in range(0, n + 1):
        j = i - 1
        while j >= 0 and height[j] > height[i]:
            max_area = max(max_area, height[j] * (i - j))
            height[j] = height[i]
            j -= 1
    return max_area


def largest_rectangle_stack(height):
    n = len(height)
    if n < 2:
        return height[0] if n else 0

    height.append(0)
    n += 1
    st = []
    max_area = i = 0
    while i < n:
        if not st or height[i] >= height[st[-1]]:
            st.append(i)
            i += 1
        else:
            idx = st[-1]
            st.pop()
            max_area = max(max_area, height[idx] * (i - st[-1] - 1 if st else i))
    return max_area


#height = [2,1,5,6,2,3]
#height = [2,1,2]
#print largest_rectangle([c for c in height])
#print largest_rectangle_stack(height)
