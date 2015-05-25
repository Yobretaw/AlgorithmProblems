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
#ENABLE_FORDWARD_CHECKING = False
ENABLE_FORDWARD_CHECKING = True

IDX_TO_PRIME = [2, 3, 5, 7, 11, 13 ,17, 19, 23]

counter = 0

def sudoku_solver(board):
    global IDX_TO_PRIME
    rows = [None] * 9
    cols = [None] * 9
    boxes = [None] * 9
    emptys = []

    for i in range(0, 9):
        rows[i] = 1
        cols[i] = 1
        boxes[i] = 1

    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != '.':
                d = IDX_TO_PRIME[int(board[i][j]) - 1]
                rows[i] *= d
                cols[j] *= d
                boxes[i - i % 3 + int(j / 3)] *= d
            else:
                emptys.append((i, j))

    for i in range(0, 9):
        board[i] = [c for c in board[i]]

    if sudoku_solver_help(board, emptys, rows, cols, boxes):
      for i in range(0, 9):
          print(' '.join(board[i]))
          board[i] = ' | '.join(board[i])
    else:
      print("NO SOLUTION FOUND")


def sudoku_solver_help(board, emptys, rows, cols, boxes):
    next_pos = find_next_pos(board, emptys)
    #global counter
    if not next_pos:
        #print(counter)
        #counter += 1
        return True

    i, j = next_pos
    emptys.pop()
    for x in range(1, 10):
        if is_valid_put(board, i, j, x, rows, cols, boxes):
            board[i][j] = str(x)
            d = IDX_TO_PRIME[x - 1]
            rows[i] *= d
            cols[j] *= d
            boxes[i - i % 3 + int(j / 3)] *= d
            d = IDX_TO_PRIME[x - 1]

            if ENABLE_FORDWARD_CHECKING and not forwardChecking(board, i, j, rows, cols, boxes):
                rows[i] /= d
                cols[j] /= d
                boxes[i - i % 3 + int(j / 3)] /= d
                board[i][j] = '.'
                continue

            if sudoku_solver_help(board, emptys, rows, cols, boxes):
                return True

            rows[i] /= d
            cols[j] /= d
            boxes[i - i % 3 + int(j / 3)] /= d
            board[i][j] = '.'
    emptys.append(next_pos)
    return False


def forwardChecking(board, row, col, rows, cols, boxes):
  PRIME_PRODUCT = 223092870
  for i in range(0, 9):
    if (board[row][i] == '.' and ((rows[row] * cols[i] % PRIME_PRODUCT == 0))) or \
        (board[i][col] == '.' and (rows[i] * cols[col] % PRIME_PRODUCT == 0)):
        print(row, col, i)
        return False
  return True

def find_next_pos(board, emptys):
    try:
        res = emptys[-1]
        return res
    except:
        return None

def is_valid_put(board, row, col, val, rows, cols, boxes):
    d = IDX_TO_PRIME[val - 1]
    return rows[row] % d != 0 and cols[col] % d != 0 and boxes[row - row % 3 + int(col / 3)] % d != 0

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

#print('int grid[N][N] = {')
#for line in board4:
#    s = '{'
#    for c in line:
#        s += (c if c != '.' else '0') + ', '
#    s = s[:-1]
#    s += '},'
#    print(s)
#print('};')

times = []
for i in range(0, 1):
  board = board4
  start_time = time.time()
  sudoku_solver(copy.deepcopy(board))
  #for line in board:
  #    print(' -' + '--' * 17)
  #    print('| ' + line + ' |')
  #print(' -' + '--' * 17)
  #print(i)
  end_time= time.time()
  times.append(end_time - start_time)

#print(mean(times))
#print(stdev(times))
