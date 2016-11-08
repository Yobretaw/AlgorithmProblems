import sys
import math

"""
    Design an algorithm that takes as input string s1, s2 and t, and determines
    if t is an interleaving of s1 and s2.
"""
def test_interleaving(t, s1, s2):
        m, n = len(s1), len(s2)
        if m + n != len(t):
            return False

        # f[i][j] is true if t[:i + j] is an interleaving of s1[:i]  and s2[:j]
        f = [[False for i in range(n + 1)] for j in range(m + 1)]
        f[0][0] = True

        for i in range(1, m + 1):
            if t[i - 1] == s1[i - 1]:
                f[i][0] = True
            else:
                break

        for i in range(1, n + 1):
            if t[i - 1] == s2[i - 1]:
                f[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = s1[i - 1] == t[i + j - 1] and f[i - 1][j] or \
                        s2[j - 1] == t[i + j - 1] and f[i][j - 1]
        
        return f[-1][-1]


if __name__ == '__main__':
    s1 = 'gtaa'
    s2 = 'atc'

    t = 'gattaca'
    print test_interleaving(t, s1, s2)

    t = 'gtataac'
    print test_interleaving(t, s1, s2)

    t = 'gatacta'
    print test_interleaving(t, s1, s2)
