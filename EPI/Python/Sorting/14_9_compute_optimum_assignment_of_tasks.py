import sys
import math
import itertools
import string
from collections import Counter


"""
    Design an algorithm that takes as input an array of numbers, which are the
    durations of the tasks, and computes a set of pairs of tasks such that the
    maximum pair sum is minimum. Each task must be in exactly one pair.

    For example, if the durations are 5, 2, 1, 6, 4, 4, then the grouping (2, 5),
    (1, 6), (4, 4) is an optimum grouping assignment - all tasks will finish by
    time 8.
"""
def compute_optimum_assignment(durations):
    # assume there are even number of tasks in <durations>.
    n = len(durations)
    if n < 3:
        return 0 if not n else sum(durations)

    durations.sort()

    res = []
    i, j = 0, n - 1
    while i < j:
        res.append((durations[i], durations[j]))
        i += 1
        j -= 1
    return res


if __name__ == '__main__':
    durations = [5, 2, 1, 6, 4, 4]
    print compute_optimum_assignment(durations)
