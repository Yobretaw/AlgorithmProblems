import sys
import os
import math
from copy import deepcopy


"""
    Implement a Sudoku solver. Your program should read an instance of Sudoku
    from command line. The command line argument is a sequence of 3-digit
    strings, each encoding a row, a column, and a digit at that location
"""
def solve_sudoku(board):
    n = len(board)

    row_set = [set() for i in range(n)]
    col_set = [set() for i in range(n)]
    box_set = [set() for i in range(n)]

    empties = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                empties.append((i, j))

    res = []
    solve_sudoku_help(board, empties, row_set, col_set, box_set, res)
    return res

def solve_sudoku_help(board, empties, row_set, col_set, box_set, res):
    if not empties:
        res.append(deepcopy(board))
        return True

    x, y = empties[-1]
    empties.pop()
    for i in range(1, len(board) + 1):
        if i in row_set[x] or i in col_set[y] or i in box_set[x - x % 3 + y / 3]:
            continue

        row_set[x].add(i)
        col_set[y].add(i)
        box_set[x - x % 3 + y / 3].add(i)
        board[x][y] = i

        if solve_sudoku_help(board, empties, row_set, col_set, box_set, res):
            return True

        board[x][y] = 0
        row_set[x].remove(i)
        col_set[y].remove(i)
        box_set[x - x % 3 + y / 3].remove(i)

    empties.append((x, y))
    return False

def print_sudoku(board):
    for line in board:
        print ' '.join(map(lambda x: str(x), line))


if __name__ == '__main__':
    board = [
            "..9748...",
            "7........",
            ".2.1.9...",
            "..7...24.",
            ".64.1.59.",
            ".98...3..",
            "...8.3.2.",
            "........6",
            "...2759.."
    ]
    board = [map(lambda x: int(x), list(line.replace('.', '0'))) for line in board]

    res = solve_sudoku(board)
    for r in res:
        print_sudoku(r)
        print '-' * 20
