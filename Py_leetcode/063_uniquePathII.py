import sys
import os
import math

"""
    Follow up for "Unique Paths":

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

    For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

    The total number of unique paths is 2.
"""
def unique_path_ii(grid):
    m = len(grid)
    n = len(grid[0])

    if grid[0][0] or grid[m - 1][n - 1]:
        return 0

    grid[0][0] = 1
    for i in range(1, n):
        grid[0][i] = grid[0][i - 1] if not grid[0][i] else 0
    for j in range(1, m):
        grid[j][0] = grid[j - 1][0] if not grid[j][0] else 0

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1] if not grid[i][j] else 0

    return grid[m - 1][n - 1]


#grid = [
#    [0,0,0],
#    [0,1,0],
#    [0,0,0]
#]
#print unique_path_ii(grid)
