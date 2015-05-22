import sys
import math

"""
    Determine if a Sudoku is valid.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

    Note:
    A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
def is_valid_sudoku(board):
    return check_row(board) and check_column(board) and check_box(board)

def check_row(board):
    for i in range(0, 9):
        filled = [0] * 9
        for j in range(0, 9):
            try:
                curr = int(board[i][j]) - 1
                if filled[curr]:
                    return False
                filled[curr] = 1
            except:
                pass
    return True

def check_column(board):
    for i in range(0, 9):
        filled = [0] * 9
        for j in range(0, 9):
            try:
                curr = int(board[j][i]) - 1
                if filled[curr]:
                    return False
                filled[curr] = 1
            except:
                pass
    return True

def check_box(board):
    for i in range(0, 3):
        for j in range(0, 3):
            filled = [0] * 9
            for a in range(0, 3):
                for b in range(0, 3):
                    try:
                        curr = int(board[3 * i + a][3 * j + b])
                        if filled[curr]:
                            return False
                        filled[curr] = 1
                    except:
                        pass
    return True

#board = [
#  "3.9....42",
#  ".189436..",
#  "......89.",
#  "..3.9..6.",
#  "427...589",
#  ".6..8.2..",
#  ".72......",
#  "..457632.",
#  "63....7.4"
#]

#for line in board:
#    print line

#print is_valid_sudoku(board)
