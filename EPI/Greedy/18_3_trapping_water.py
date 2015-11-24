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
    l, r = 0, n - 1
    l_max = heights[0]
    r_max = heights[-1]

    while l < r:
        if heights[l] < heights[r]:
            res += l_max - heights[l]
            l += 1
        else:
            res += r_max - heights[r]
            r -= 1
        
        l_max = max(l_max, heights[l])
        r_max = max(r_max, heights[r])

    return res


"""
    Variant 18.3.1

    Solve the same problem with an algorithm that accesses elements in input array
    in order and can read an element only once. Use minimum additional space.
"""
# Time: O(n), space: O(n) in worst case
def trapping_water2(heights):
    n = len(heights)
    if n < 2:
        return 0

    # f is a stack of tuple (width, height) tuple in decreasing order of height.
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

            # This loop will execute at most len(heights) times
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
