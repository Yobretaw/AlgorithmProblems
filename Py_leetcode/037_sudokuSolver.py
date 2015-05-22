import sys
import math
import imp
import time
import copy
#from sets import Set
from statistics import mean, stdev

is_valid_sudoku = imp.load_source('Node', './036_validSudoku.py').is_valid_sudoku

"""
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    Empty cells are indicated by the character '.'

    You may assume that there will be only one unique solution.
"""
FC_CHECKING = False
#FC_CHECKING = True
def sudoku_solver(board):
    A = [[None for j in range(0, 9)] for i in range(0, 9)]
    for a in A:
        for i in range(0, 9):
            a[i] = [False for i in range(1, 10)]

    for i in range(0, 9):
        board[i] = [c for c in board[i]]
    sudoku_solver_help(board, A)
    for i in range(0, 9):
        board[i] = ' | '.join(board[i])


def sudoku_solver_help(board, A):
    next_pos = find_next_pos(board)
    if not next_pos:
        return True

    i, j = next_pos
    for x in range(1, 10):
        if FC_CHECKING:
            if A[i][j][x - 1]: continue
        if is_valid_put(board, i, j, str(x)):
            board[i][j] = str(x)
            if FC_CHECKING:
                if A[i][j][x - 1]: continue
            add_num_to_sets(A, i, j, x)
            if sudoku_solver_help(board, A):
                return True
            board[i][j] = '.'
            if FC_CHECKING:
                remove_num_from_sets(A, i, j, x)
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

"""
    Methods used in forward checking
"""
def remove_num_from_sets(A, row, col, val):
    for i in range(0, 9):
        A[row][i][val - 1] = False
        A[i][col][val - 1] = False

def add_num_to_sets(A, row, col, val):
    for i in range(0, 9):
        A[row][i][val - 1] = True
        A[i][col][val - 1] = True


"""
    Optimization

    1. Forward checking: maintain a 9x9 array A where A[i][j] is a set of numbers. Initally all sets have integers from 1 to 9.
    2. CSP Heuristics(most contrained variable, most constraining variable and least constraining variable).
"""


#board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board1 = [
  "3.9....42",
  ".189436..",
  "......89.",
  "..3.9..6.",
  "427...589",
  ".6..8.2..",
  ".72......",
  "..457632.",
  "63....7.4"
]
board2 = [
  "...12..3.",
  "..3.8..16",
  "4..53..9.",
  ".1.8..52.",
  ".4.....6.",
  ".68..2.7.",
  ".8..93..2",
  "69..5.3..",
  ".3..48...",
]
board3 = [
  "6..8.9...",
  "..5..7.86",
  ".7.......",
  "...4.13.7",
  "8.1...5.4",
  "7.92.5...",
  ".......4.",
  "18.5..6..",
  "...3.4..5",
]
board4 = [
  "1........",
  "7....81.2",
  ".63.5....",
  ".7.39....",
  "..58.46..",
  "....25.4.",
  "....1.87.",
  "2.89....3",
  "........6",
]
times = []
for i in range(0, 50):
  start_time = time.time()
  sudoku_solver(copy.deepcopy(board1))
  #for line in board:
  #    print ' -' + '--' * 17
  #    print '| ' + line + ' |'
  #print ' -' + '--' * 17
  print(i)
  end_time= time.time()
  times.append(end_time - start_time)

print(mean(times))
print(stdev(times))
