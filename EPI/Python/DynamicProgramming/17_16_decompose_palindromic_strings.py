import sys
import math

"""
    How would you compute a palindromic decompositions of a string s that uses
    a minimum number of substrings.
"""
def compute_palindromic_decompositions(s):
    n = len(s)
    if n < 2:
        return [s]
    
    # t[i][j] is true if s[i:j + 1] is a palindrome
    t = [[False for i in range(n)] for j in range(n)]

    # f[i] is the minimum number of substrings required for the ith suffix
    # of s
    f = [i for i in range(n + 1)][::-1]

    for i in reversed(range(0, n)):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or t[i + 1][j - 1]):
                t[i][j] = True
                f[i] = min(f[i], 1 + f[j + 1])

    return f[0]

if __name__ == '__main__':
    print compute_palindromic_decompositions('0204451881')
