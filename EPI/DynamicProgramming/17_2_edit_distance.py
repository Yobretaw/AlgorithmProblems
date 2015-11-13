import sys
import math


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


if __name__ == '__main__':
    a = 'abc'
    b = 'cbaa'
    print edit_distance(a, b)
