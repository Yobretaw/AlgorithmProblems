import sys
import os
import math

"""
    A number of apartment building are coming up on a new street. The postal
    service wants to place a single mailbox on the street. Their objective
    is to minimize the total distance that residents have to walk to collect
    their mail each day.

    Devise an algorithm tha compute where to place the mailbox so as to minimize
    the total distance, that residents travel to get to the mailbox.
"""
def find_closest_pos(locs):
    # Assume locations are sorted in increasing order
    n = len(locs)
    if n < 2:
        return -1 if not n else locs[0]

    if n % 2 == 1:
        return locs[n / 2]
    else:
        return (locs[n / 2] + locs[n / 2 + 1]) / 2
