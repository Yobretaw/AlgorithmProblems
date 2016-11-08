import sys
import os
import re
import math
import random

"""
    ============================================================================================
    Write a function which takes as input a 2D array A of 1s and 0s, set all positions to 0 if
    its rows and columns has at least one 0s.
    ============================================================================================
"""
def outputPositions(board):
    n = len(board)
    if n == 0:
        return []

    m = len(board[0])
    if m == 0:
        return []

    one_rows = {}
    one_cols = {}
    for i in range(0, n):
        for j in range(0, m):
            if board[i][j] == 0:
                one_rows[i] = 1
                one_cols[j] = 1

    for i in range(0, n):
        for j in range(0, m):
            if one_rows.get(i) or one_cols.get(j):
                board[i][j] = 0


def outputPositionsWithoutExtraSpace(board):
    """
    This method uses constant space
    """
    n = len(board)
    if n == 0:
        return []

    m = len(board[0])
    if m == 0:
        return []

    has_first_row_zero = False
    has_first_col_zero = False

    for i in range(0, n):
        if not board[i][0]:
            has_first_col_zero = True
            break

    for j in range(0, m):
        if not board[0][j]:
            has_first_row_zero = True
            break

    for i in range(1, n):
        for j in range(1, m):
            if not board[i][j]:
                A[i][0] = A[0][j] = 0
    
    for i in range(1, n):
        if not board[i][0]:
            continue

        for j in range(1, m):
            board[i][j] = 0

    for j in range(1, m):
        if not board[0][j]:
            continue

        for i in range(1, n):
            board[i][j] = 0

    if has_first_row_zero:
        for j in range(0, m):
            board[0][j] = 0

    if has_first_col_zero:
        for i in range(0, n):
            board[i][0] = 0
