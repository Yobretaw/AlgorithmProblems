import sys
import os
import math

"""
    Write a function which takes as input a positive integer n, and returns a
    list of all distinct nonattacking placements of n queens on an n x n board.
"""
def solve(n):
    row = [0] * n
    solve_help(n, row, 0)

def solve_help(n, row, curr_row):
    if curr_row >= n:
        print_result(row)
        return

    res = False
    for col in range(0, n):
        if is_valid_placement(row, curr_row, col):
            row[curr_row] = col + 1
            if solve_help(n, row, curr_row + 1):
                res = True
            row[curr_row] = 0
    return res

def is_valid_placement(row, row_idx, col_idx):
    if col_idx + 1 in row:
        return False

    a, b, c = row_idx - 1, col_idx - 1, col_idx + 1
    while a >= 0 and (b >= 0 or c < len(row)):
        if row[a] == b + 1 or row[a] == c + 1:
            return False
        a -= 1
        b -= 1
        c += 1
    
    return True

def print_result(row):
    res = [[' . '] * len(row) for i in range(len(row))]

    for i, pos in enumerate(row):
        res[i][pos - 1] = ' Q '

    for line in res:
        print ''.join(line)
    print '=' * len(''.join(line))


if __name__ == '__main__':
    solve(12)
