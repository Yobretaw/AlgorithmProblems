import sys
import math
import imp
from collections import defaultdict
from heapq import *


"""
    We keep (height, right) pairs in the priority queue and they stay in there
    as long as there's a larger height in there.

    In each loop, we first check which has a smaller x-coordinate: adding the
    next building from the input, or removing the next building from the queue.
    In case of a tie, adding buildings wins, as that guarantees correctness.
    We then either add all input buildings starting at that x-coordinate or we
    remove all queued buildings ending at that x-coordinate or earlier (remember
    we keep buildings in the queue as long as they're "under the roof" of a
    larger actually alive building). And then, if the current maximum height in
    the queue differs from the last in the skyline, we add it to the skyline.
"""
def get_skyline(LRH):
    if not LRH:
        return []

    skyline = []
    i, n = 0, len(LRH)
    liveHR = []
    while i < n or liveHR:
        x = 0
        if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
            # the curren tallest buildings intersects with buildings from input.
            # We read from input.
            x = LRH[i][0]
            while i < n and LRH[i][0] == x:
                # push all points wit x coordination equal to x
                heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                i += 1
        else:
            # No buildings from input intersect with the current tallest building.
            # we can remove all buildings that are under the roof of the tallest one
            x = -liveHR[0][1]
            while liveHR and -liveHR[0][1] <= x:
                heappop(liveHR)

        height = -liveHR[0][0] if liveHR else 0
        if not skyline or height != skyline[-1][1]:
            skyline.append((x, height))

    return skyline

if __name__ == '__main__':
    print get_skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    # print get_skyline([[1, 3, 4], [2, 4, 4]])
    # print get_skyline([[1, 4, 4], [2, 3, 4]])
