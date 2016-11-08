import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Check whether a 9x9 2D array representing a partially completed Sudoku is valid. Specifically,
    check that no row, column, and 3x3 2D subarray contains duplicates. A 0-value in the 2D array
    indicates that entry is blank; every other entry is in [1,9]
    ============================================================================================
"""
def sudokuChecker(board):
    if not checkRow(board):
        return False

    if not checkColumn(board):
        return False

    if not checkSubarray(board):
        return False

    return True

def checkRow(board):
    for row in board:
        m = {}
        for val in row:
            if val == 0:
                continue
            if m.get(val):
                return False
            m[val] = 1

    return True

def checkCol(board):
    for i in range(0, 9):
        m = {}
        for j in range(0, 9):
            if board[j][i] == 0:
                continue
            if m.get(board[j][i]):
                return False
            m[board[j][i]] = 1

    return True

def checkSubarray(board):
    for i in range(0, 6):
        for j in range(0, 6):
            m = {}
            for m in range(0, 3):
                for n in range(0, 3):
                    val = board[i + m][j + n]

                    if val == 0:
                        continue

                    if m.get(val):
                        return False
                    m[val] = 1
    return True

