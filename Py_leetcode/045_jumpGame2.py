import sys
import math
from collections import defaultdict

"""
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.

    For example:
    Given array A = [2,3,1,1,4]

    The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
def jump_game2(A):
    if not A:
        return True

    n = len(A)
    curr_right = 0
    max_right = 0
    steps = 0
    for i in range(0, n):
        if i > max_right:
            # not possible
            return -1

        if i > curr_right:
            steps += 1
            curr_right = max_right

        max_right = max(max_right, i + A[i])

    return steps

#a = [2, 3, 1, 1, 4]
#print jump_game2(a)
