import sys
import math
import imp

is_valid_sudoku = imp.load_source('Node', './36_validSudoku.py').is_valid_sudoku

"""
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    Empty cells are indicated by the character '.'

    You may assume that there will be only one unique solution.
"""
def sudoku_solver(board):
    for i in range(0, 9):
        board[i] = [c for c in board[i]]
    sudoku_solver_help(board)
    for i in range(0, 9):
        board[i] = ''.join(board[i])


def sudoku_solver_help(board):
    next_pos = find_next_pos(board)
    if not next_pos:
        return True

    i, j = next_pos
    for x in range(1, 10):
        if is_valid_put(board, i, j, str(x)):
            board[i][j] = str(x)
            if sudoku_solver_help(board):
                return True
            board[i][j] = '.'

    return False


def find_next_pos(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '.':
                return i, j
    return None

def is_valid_put(board, row, col, val):
    for i in range(0, 9):
        if board[row][i] == val:
            return False

    for i in range(0, 9):
        if board[i][col] == val:
            return False

    row -= row % 3
    col -= col % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if board[row + i][col + j] == val:
                return False
    return True


#board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
#sudoku_solver(board)
#for line in board:
#    print line
