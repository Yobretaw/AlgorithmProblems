import sys
import math

"""
    The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
    consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left
    room and must fight his way through the dungeon to rescue the princess.

    The knight has an initial health point represented by a positive integer. If at any point his health point drops
    to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
    other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

    In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
    step.


    Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

    For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
    path RIGHT -> RIGHT -> DOWN -> DOWN.

    -2 (K)	-3	3
    -5	        -10	1
    10	        30	-5 (P)

    Notes:

    The knight's health has no upper bound.

    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the
    princess is imprisoned.
"""
def min_hp(board):
    m, n = len(board), len(board[0])
    for i in reversed(range(0, m)):
        for j in reversed(range(0, n)):
            if i < m - 1 and j < n - 1:
                board[i][j] = max(min(board[i + 1][j], board[i][j + 1]) - board[i][j], 1) 
            elif i < m - 1:
                board[i][j] = max(board[i + 1][j] - board[i][j], 1)
            elif j < n - 1:
                board[i][j] = max(board[i][j + 1] - board[i][j], 1)
            else:
                board[i][j] = max(-board[i][j], 0) + 1
    return board[0][0]


board = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

#board = [
#    [1, -3, 3],
#    [0, -2, 0],
#    [-3, -3, -3]
#]
#board = [
#    [0, -3],
#    [-10, 0]
#]
#board = [
#    [0, -5],
#    [0, 0]
#]
board = [
    [0 ,0, 0],
    [1, 1, -1]
]
print min_hp(board)
