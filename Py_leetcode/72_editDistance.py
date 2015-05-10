import sys
import os
import math

"""
    Given two words word1 and word2, find the minimum number of steps required to convert
    word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character
"""
def edit_distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if not l1 or not l2:
        return l1 if l1 else l2

    mem = [[0 for j in range(0, l2 + 1)] for i in range(0, l1 + 1)]

    for i in range(0, l1 + 1):
        mem[i][0] = i
    for j in range(0, l2 + 1):
        mem[0][j] = j
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            mem[i][j] = min(mem[i - 1][j] + 1, mem[i][j - 1] + 1)
            mem[i][j] = min(mem[i][j], mem[i - 1][j - 1] + (1 if s1[i - 1] != s2[j - 1] else 0))
    return mem[-1][-1]


#s1 = "sea"
#s2 = "eat"
#print edit_distance(s1, s2)
