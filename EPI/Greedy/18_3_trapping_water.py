import sys
import math


"""
    A one-dimentional container is specified by an array of n nonnegative integers,
    specifying the height of each unit-width rectangle. Design an algorithm for
    computing the capacity of the container.
"""
def trapping_water(heights):
    n = len(heights)
    if n < 2:
        return 0

    res = 0
    left_idx, right_idx = 0, n - 1
    left_max = heights[0]
    right_max = heights[-1]

    while left_idx < right_idx:
        if heights[left_idx] < heights[right_idx]:
            res += left_max - heights[left_idx]
            left_idx += 1
        else:
            res += right_max - heights[right_idx]
            right_idx -= 1
        
        left_max = max(left_max, heights[left_idx])
        right_max = max(right_max, heights[right_idx])

    return res


"""
    Variant 18.3.1

    Solve the same problem with an algorithm that accesses elements in input array
    in order and can read an element only once. Use minimum additional space.
"""
def trapping_water2(heights):
    n = len(heights)
    if n < 2:
        return 0

    f = []
    f.append((1, heights[0]))

    res = 0
    for i in range(1, n):
        h = heights[i]
        if h < f[-1][1]:
            f.append((1, h))
        else:
            idx = len(f)
            while idx > 0 and f[idx - 1][1] <= h:
                idx -= 1
            
            width = 0
            left_height = h if idx > 0 else f[0][1]
            for j in range(idx, len(f)):
                res += (left_height - f[j][1]) * f[j][0]
                width += f[j][0]

            if idx == 0:
                # current one is higher than all previous heights
                f = [(1, h)]
            else:
                f[idx:] = [(width + 1, left_height)]

    return res


if __name__ == '__main__':
    heights = [1, 2, 1, 3, 4, 4, 5, 1, 2, 0, 3]
    print trapping_water(heights)
    print trapping_water2(heights)

    heights = [0, 2, 0]
    print trapping_water(heights)
    print trapping_water2(heights)

    heights = [5, 2, 1, 2, 1, 5]
    print trapping_water(heights)
    print trapping_water2(heights)
