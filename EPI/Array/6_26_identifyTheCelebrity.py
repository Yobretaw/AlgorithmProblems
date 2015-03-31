import sys
import os
import re
import math
import random

"""
    ============================================================================================
    For any two distinct people a and b, a may or may not know b. In the context of this problem,
    the "knows" relation is not necessary symmetric: a may know b, but b may not know a. At a
    party, every one knows someone else. Now a celebrity joins the party - everyone knows him, but
    he knows no one.

    Let F be a n x n boolean 2D array repersenting the "knows" relations for n people - F[a][b]
    is true if and only if a knows b. Design an algorithm to find the celebrity.
    ============================================================================================
"""
def findCelebrity(F):
    """
        Brute force: The goal is to find a column with all 1's except for one spot which is the
        celebrity himself.
    """
    m = len(F)
    n = len(F[0])

    for j in range(0, n):
        count = 0
        for i in range(0, m):
            if m[i][j] == False and i != j:
                break
            count += 1

        if count == m:
            i = 0
            while i < n and F[i][j] == False:
                i += 1

            if i == n:
                return j

def findCelebrity2(F):
    """
        The challenge to avoid having to look at all of F, which result in a O(n^2) time complexity.

        The key to achieving time efficiency is to process people in order, and eliminate at least
        one people from the set with each lookup into F. We begin by checking F[0][1], i.e, the
        relation between Person 0 and Person 1.
        
        Suppose we check F[i][j] where i < j. The problem statement guarantees that if F[i][j] is false,
        j is not celebrity and i is still a possible celebrity candidate. Hence we eliminate j from
        the set of celebrity and move to F[i][j + 1].

        If F[i][j] is true, than Person i cannot be the celebrity, and for all j' < j, j' is not a celebrity
        because F[i][j'] must be false. We then move to F[j][j + 1] since i < j.

        Time complexity: O(n), space O(1)
    """
    i = 0
    j = 1
    while j < len(F):
        if F[i][j]:
            i += j

        # we need to increment j both when F[i][j] is true or fales
        j += 1

    return i
