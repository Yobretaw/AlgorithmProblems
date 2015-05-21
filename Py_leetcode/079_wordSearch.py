import sys
import os
import math
from collections import defaultdict
import copy

"""
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
    cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

    For example,
    Given:

    board = [
      ["ABCE"],
      ["SFCS"],
      ["ADEE"]
    ]

    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
"""
def word_search(board, word):
    if not word:
        return False

    visited = [[0 for j in range(0, len(board[0]))] for i in range(len(board))]
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == word[0]:
                if word_search_help(board, i, j, visited, 0, word):
                    return True
    return False

def word_search_help(board, i, j, visited, idx, word):
    if idx == len(word):
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != word[idx] or visited[i][j]:
        return False

    idx += 1
    visited[i][j] = 1
    ret = word_search_help(board, i - 1, j, visited, idx, word) or word_search_help(board, i + 1, j, visited, idx, word) or word_search_help(board, i, j - 1, visited, idx, word) or word_search_help(board, i, j + 1, visited, idx, word)
    visited[i][j] = 0
    return ret


#print word_search(["aaaa","aaaa","aaaa"], 'aaaaaaaaaaaaa')

#board = ["ABCE", "SFCS", "ADEE"]
#print word_search(board, 'ABCCED')
#print word_search(board, 'SEE')
#print word_search(board, 'ABCB')
