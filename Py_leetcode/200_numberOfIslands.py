import sys
import os
import re
import math
from collections import deque

"""
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is
    surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
    may assume all four edges of the grid are all surrounded by water.

    Example 1:

    11110
    11010
    11000
    00000

    Answer: 1

    Example 2:

    11000
    11000
    00100
    00011

    Answer: 3
"""
def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    for i in range(0, m):
        grid[i] = list(grid[i])

    res = 0
    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == '1':
                bfs(grid, i, j)
                res += 1
    return res

def bfs(grid, i, j):
    m, n = len(grid), len(grid[0])

    q = deque()
    q.append((i, j))
    while q:
        i, j= q[0]
        q.popleft()

        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            continue

        grid[i][j] = '2'
        q.append((i - 1, j))
        q.append((i + 1, j))
        q.append((i, j - 1))
        q.append((i, j + 1))

    return

grid = [
    '11110',
    '11010',
    '11000',
    '00000',
]
print num_islands(grid)
