import sys
import math


"""
    You are playing a board game in which you can move 1 to k steps at a time.
    You need to make exactly n steps to get to your destination.

    write a function which takes as input n and k, and returns the number of
    ways in which you can advance to the destination.

    For example, if n = 4 and k = 2, there are five ways in which to advance:

            <1, 1, 1, 1>,
            <1, 1, 2>,
            <1, 2, 1>,
            <2, 1, 1>,
            <2, 2>
"""
# Native recursion method
def count_ways_to_dest(n, k):
    res = []
    count_ways_to_dest_help(n, k, 0, [], res)
    return res

def count_ways_to_dest_help(n, k, total, path, res):
    if total == n:
        res.append(list(path))
        return

    i = 1
    while i <= k and total + i <= n:
        path.append(i)
        count_ways_to_dest_help(n, k, total + i, path, res)
        path.pop()
        i += 1

# DP
def count_ways_to_dest_dp(n, k):
    if n <= 1:
        return 1

    # f[i][j] represents the number of ways to reach i using the first j steps
    # we the have f[i][j] = Sum_{i from 1 to k}(f[i - k][j])
    f = [[0 for i in range(k + 1)] for j in range(n + 1)]
    f[0] = f[1] = [1] * (k + 1)

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            f[i][j] = sum(f[i - x][j] for x in range(1, min(i + 1, k + 1)))

    return f[-1][-1]


# optimized DP, use less space as only k of those entries are ever needed at a
# time, so the problem can be solved with O(k) additional space.
def count_ways_to_dest_dp2(n, k):
    if n <= 1:
        return 1

    steps = [0] * (k + 1)
    steps[0] = steps[1] = 1
    for i in range(2, n + 1):
        steps[i % (k + 1)] = 0
        for j in range(1, min(k + 1, i + 1)):
            steps[i % (k + 1)] += steps[(i - j) % (k + 1)]

    return steps[n % (k + 1)]


if __name__ == '__main__':
    for i in range(5, 10):
        for j in range(1, i):
            print i, j, len(count_ways_to_dest(i, j)), count_ways_to_dest_dp(i, j), count_ways_to_dest_dp2(i, j)
