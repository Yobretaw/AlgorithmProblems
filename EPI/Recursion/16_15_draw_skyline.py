import sys
import os
import math


"""
    A number of buildings are visible from a point. Each building is a rectangle,
    and the bottom of each building lies on a fixed line. A building is specified
    using its left and right coordinates, and its height. One building may partly
    obstruct another. The skyline is the list of coordinates and corresponding
    heights of what is visible.

    Design an efficient algorithm for computing the skyline.
"""
class Building:
    def __init__(self, left, right, height):
        self.left, self.right, self.height = left, right, height;

    def __cmp__(self, other):
        if self.left != other.left:
            return self.left - other.left
        else:
            return self.right - other.right

    def __repr__(self):
        return '(%s, %s, %s)' % (self.left, self.right, self.height)

def compute_skyline(buildings):
    buildings.sort()
    buildings = compute_skyline_help(buildings)

    return buildings

    # If the required output is a list of "key points" that uniquely defines a
    # skyline, uncomment the code below.
    # A key point is the left endpoint of a horizontal line segment.
    
    #res = []
    #for b in buildings:
    #    res.extend([(b.left, b.height), (b.right, b.height)])
    
    #for i in range(1, len(res)):
    #    if res[i - 1] and res[i] and res[i][1] == res[i - 1][1]:
    #        if i < len(res) - 1 and res[i + 1][0] == res[i][0]:
    #            res[i] = None
    #        else:
    #            res[i] = tuple([res[i][0], 0])

    #return filter(None, res)


def compute_skyline_help(buildings):
    n = len(buildings)
    if not n:
        return []

    if n == 1:
        return buildings

    l = compute_skyline_help(buildings[:n/2])
    r = compute_skyline_help(buildings[n/2:])

    return merge_buildings(l, r)

def merge_buildings(l, r):
    i = j = 0
    merged = []

    while i < len(l) and j < len(r):
        if l[i].right < r[j].left:
            merged.append(l[i])
            i += 1
        elif r[j].right < l[i].left:
            merged.append(r[j])
            j += 1
        elif l[i].left <= r[j].left:
            l_idx = [i]
            r_idx = [j]
            merge_help(merged, l[i], l_idx, r[j], r_idx)
            i, j = l_idx[0], r_idx[0]
        else:
            l_idx = [i]
            r_idx = [j]
            merge_help(merged, r[j], r_idx, l[i], l_idx)
            i, j = l_idx[0], r_idx[0]

    merged.extend(l[i:])
    merged.extend(r[j:])
    return merged

def merge_help(merged, a, a_idx, b, b_idx):
    i, j = a_idx[0], b_idx[0]

    if a.right <= b.right:
        if a.height > b.height:
            if b.right != a.right:
                merged.append(a)
                i += 1
                b.left = a.right
            else:
                j += 1
        elif a.height == b.height:
            b.left = a.left
            i += 1
        else:
            if a.left != b.left:
                merged.append(Building(a.left, b.left, a.height))
            i += 1
    else:
        if a.height >= b.height:
            j += 1
        else:
            if a.left != b.left:
                merged.append(Building(a.left, b.left, a.height))
            a.left = b.right
            merged.append(b)
            j += 1

    a_idx[0], b_idx[0] = i, j
    

if __name__ == '__main__':
    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
    buildings = [Building(a[0], a[1], a[2]) for a in buildings]

    print compute_skyline(buildings)
