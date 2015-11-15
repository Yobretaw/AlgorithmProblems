import sys
import math


"""
    Given two words word1 and word2, find the minimum number of steps required
    to convert word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character    
"""
def edit_distance(a, b):
    m, n = len(a), len(b)
    if not m or not n:
        return m if not n else n

    t = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        t[i][0] = i
    for i in range(n + 1):
        t[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1]
            else:
                t[i][j] = min(t[i - 1][j - 1], t[i - 1][j], t[i][j - 1]) + 1
    return t[-1][-1]

# O(n) space
def edit_distance2(a, b):
        m, n = len(a), len(b)
        if not m or not n:
            return m if not n else n

        t = [i for i in range(n + 1)]
        for i in range(1, m + 1):
            prev_i_1_j_1 = t[0]
            t[0] = i
            for j in range(1, n + 1):
                prev_i_1_j = t[j]
                if a[i - 1] == b[j - 1]:
                    t[j] = prev_i_1_j_1
                else:
                    t[j] = min(t[j - 1], t[j], prev_i_1_j_1) + 1
                
                prev_i_1_j_1 = prev_i_1_j

        return t[-1]


"""
    Variant 17.2.1

    Given A and B as above, compute a longest sequence of characters that is a
    subsequence of both A and B.
"""
def compute_longest_common_subsequence_length(a, b):
    if not a or not b:
        return 0
    
    m, n = len(a), len(b)
    t = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[-1][-1]

def compute_longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    m, n = len(a), len(b)
    t = [[0 for i in range(n + 1)] for j in range(m + 1)]
    prev = [[(0, 0) for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
                prev[i][j] = (1, 1)
            else:
                if t[i - 1][j] > t[i][j - 1]:
                    t[i][j] = t[i - 1][j]
                    prev[i][j] = (1, 0)
                else:
                    t[i][j] = t[i][j - 1]
                    prev[i][j] = (0, 1)

    res = []
    i, j = m, n
    while i >= 1 and j >= 1:
        left, up = prev[i][j]
        if left and up:
            res.append(a[i - 1])
            i, j = i - 1, j - 1
        else:
            i, j = i - left, j - up

    return ''.join(res[::-1])


"""
    Variant 17.2.2

    Given a string A, compute the minimum number of characters you need to
    delete from A to make the resulting string a palindrome.
"""
def compute_min_removed_char(a):
    n = len(a)
    if n < 2:
        return 0

    # t[i][j] is the minimum nubmer of characters need to be deleted to make
    # substring a[i...j] a palindrome
    t = [[0 for i in range(n)] for j in range(n)]

    for i in range(n - 1):
        t[i][i + 1] = int(a[i] != a[i + 1])

    
    for i in range(n):
        for j in range(i + 2, n):
            if a[i] == a[j]:
                t[i][j] = t[i + 1][j - 1]
            else:
                t[i][j] = min(t[i + 1][j], t[i][j - 1]) + 1

    return t[0][-1]




if __name__ == '__main__':
    a = 'abc'
    b = 'cbaa'
    a = '1234'
    b = '1224533324'
    a = 'thisisatest'
    b = 'testing123testing'
    #a = 'XMJYAUZ'
    #b = 'MZJAWXU'
    #a = 'AGGTAB'
    #b = 'GXTXAYB'
    #a = b = 'a'
    #print edit_distance(a, b)
    #print edit_distance2(a, b)

    #print compute_longest_common_subsequence(a, b)
    print compute_min_removed_char('abc')
    print compute_min_removed_char('ab')
    print compute_min_removed_char('aa')
    print compute_min_removed_char('aaa')
