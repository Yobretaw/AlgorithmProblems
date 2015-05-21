import sys
import os
import math

"""
    Given an integer n, return all distinct solutions to the n-queens puzzle.

    Each solution contains a distinct board configuration of the n-queens' placement,
    where 'Q' and '.' both indicate a queen and an empty space respectively.

    For example,
    There exists two distinct solutions to the 4-queens puzzle:

    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
"""
def n_queens(n):
    res = []
    curr = ['.'] * n
    n_queens_help(0, curr, res)
    return res


def n_queens_help(idx, curr, res):
    n = len(curr)
    if idx == n:
        res.append(generate_board(curr))
        return True
    
    for x in range(0, n):
        if is_valid_put(curr, idx, x):
            curr[idx] = x
            n_queens_help(idx + 1, curr, res)
            curr[idx] = None


def is_valid_put(arr, idx, x):
    for i in range(0, idx):
        if arr[i] == x or arr[i] == x - idx + i or arr[i] == x + idx - i:
            return False
    return True


def generate_board(arr):
    n = len(arr)
    board = [['.'] * n for i in range(0, n)]
    for i in range(0, n):
        board[i][arr[i]] = 'Q'
    return [''.join(board[i]) for i in range(0, n)]

#for sol in n_queens(10):
#    for line in sol:
#        print line
#    print '-' * 100

