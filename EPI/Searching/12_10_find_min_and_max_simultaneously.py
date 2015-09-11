import sys
import os
import math

"""
    Find the indices of min and max values in an array using less than 2(n - 1)
    comparsions

    ========================

    One way to think of this problem is that we are searching for the strongest
    and weakest players in a group of players, assuming players are totaly
    ordered. There is no point in looking at any players who won a game when
    we want to find the weakest player. The better approach is to play n / 2
    matches between disjoint pairs of players. The strongest player will come
    from the n / 2 winners and the weakest players will come from the n / 2
    losers.

    Following the above analogy, we partition the array into min candidate and
    max candidates by comparing successive pairs - this will give us n / 2
    candidates for min and n / 2 candidates for max at the cost of n / 2
    comparsions. It takes n / 2 - 1 comparsions to find the min from the min
    candidates, and it takes n / 2 - 1 comparsions to find the max from the max
    candidates, yielding a total of 3n / 2 - 2 comparsions.
"""
def find_min_max(arr):
    n = len(arr)
    if n < 2:
        return None if not arr else arr[0]

    d = [0] * (n)
    for i in range(n - 1):
        d[i] = arr[i] > arr[i + 1]
    d[-1] = not d[-2]

    min_players = [arr[x] for x in range(len(d)) if not d[x]]
    max_players = [arr[x] for x in range(len(d)) if d[x]]

    a = b = 0
    for i in range(1, len(min_players)):
        if min_players[a] > min_players[i]:
            a = i
    
    for i in range(1, len(max_players)):
        if max_players[b] < max_players[i]:
            b = i

    return min_players[a], max_players[b]

#A = [3, 2, 5, 1, 2, 4]
#print find_min_max(A)
