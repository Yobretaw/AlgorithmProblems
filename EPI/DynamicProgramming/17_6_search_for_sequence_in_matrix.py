import sys
import math
from collections import deque, OrderedDict

"""
    Design an algorithm that takes as input a matrix A, and an array S, and
    determines whether S appears in A. If S appears in A, print the sequence
    of entries where it appears.

    For example, if

        A = [
            [1, 2, 3],
            [3, 4, 5],
            [5, 6, 7]
        ]

    and S = [1, 3, 4, 2], then S occurs in A, and the entries are

        (0, 0), (1, 0), (1, 1), (0, 1)
"""
def search_seq_in_matrix(mtx, s):
    m, n = len(mtx), len(mtx[0])

    for i in range(m):
        for j in range(n):
            res = bfs(mtx, s, i, j)
            if res:
                print res
                return True
    return False

def bfs(mtx, s, i, j):
    m, n = len(mtx), len(mtx[0])

    q = deque()
    q.append((0, [(0, 0)]))
    while q:
        idx, seq = q[0]
        q.popleft()

        i, j = seq[-1]

        if i < 0 or i >= m or j < 0 or j >= n or mtx[i][j] != s[idx]:
            continue

        if idx == len(s) - 1:
            return seq

        if (i - 1, j) not in seq:
            q.append((idx + 1, seq + [(i - 1, j)]))
        if (i + 1, j) not in seq:
            q.append((idx + 1, seq + [(i + 1, j)]))
        if (i, j - 1) not in seq:
            q.append((idx + 1, seq + [(i, j - 1)]))
        if (i, j + 1) not in seq:
            q.append((idx + 1, seq + [(i, j + 1)]))

    return []


"""
    If no duplicates in matrix, then two methods could be used:

    METHOD 1.

        1) Create a hash table with character as a key and value representing
        the coordinates of the character present in the matrix. 

        2) if The search string is "rat",then search for the first character
        in the hash map and find its coordinates. 

        3) After this search for the second character in the hash table and find
        its coordinates and find the relationship("r") between the coordinates
        of the first char and the second char,whether it lies in the left straight
        or right straight or diagonal. 

        4) After this see for the third char and check for the relationship of
        its coordinate with the coordinate of its last char and if it matches
        with the "r" ,then continue else return false. 

        5) Continue this process till the end of the string . 

        Time complexity : 
        1) In creating hash table : O(m*n) 
        2) search for string occurence : O (l) : l is the string length

    METHOD 2.

        If the matrix is fixed, then we can build a trie that contains all
        possible words from that matrix. Search a word against the trie takes
        O(len(s)) time.
"""
def search_seq_in_matrix2(mtx, s):
    m, n = len(mtx), len(mtx[0])
    
    posToChar = {}
    charToPos = {}
    for i in range(m):
        for j in range(n):
            posToChar[(i, j)] = mtx[i][j]
            charToPos[mtx[i][j]] = (i, j)

    # generate the sequence of positions
    positions = [charToPos[c] for c in s]

    # if there are duplicates, return False
    if len(positions) != len(set(positions)):
        return False

    # compare adjacent positions
    for i in range(1, len(positions)):
        prev_x, prev_y = positions[i - 1]
        curr_x, curr_y = positions[i]

        if abs(prev_x - curr_x) + abs(prev_y - curr_y) != 1:
            return False

    print positions
    return True


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7]
    ]

    s = [1, 3, 5, 6, 7, 5, 3, 2, 4]
    print search_seq_in_matrix(A, s)

    A = [
        [1, 3, 3],
        [3, 4, 5],
        [4, 5, 7]
    ]

    #s = [1, 3, 3, 5]
    s = [1, 3, 4, 5, 7, 5, 3, 3, 4]
    print search_seq_in_matrix(A, s)


    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = [1, 4, 7, 8, 9, 6, 3, 2, 5]
    print search_seq_in_matrix2(A, s)

    s = [1, 5]
    print search_seq_in_matrix2(A, s)
