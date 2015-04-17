import sys
import math

"""
    Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
    and there exists one unique longest palindromic substring.
"""
def longestPalindrome(s):
    if not s or len(s) == 1:
        return s

    s1 = '#'.join(list(s))
    s1 = '#' + s1 + '#'

    n = len(s1)
    f = [0] * n
    mid = right = pos = 0
    l = 1
    for i in range(1, n):
        if right > i:
            f[i] = min(f[2 * mid - i], right - i)
        else:
            f[i] = 0

        while i - f[i] - 1 >= 0 and i + f[i] + 1 < n and s1[i - f[i] - 1] == s1[i + f[i] + 1]:
            f[i] += 1

        if l < f[i]:
            l = f[i]
            pos = (i - f[i]) / 2
        
        if right < i + f[i]:
            mid = i
            right = i + f[i]

    return s[pos:pos + l]


def longestPalindrome_dp(s):
    if not s or len(s) == 1:
        return s

    n = len(s)
    mem = []
    for i in range(0, n):
        mem.append([0] * n)

    for i in range(0, n):
        mem[i][i] = 1

    for i in range(0, n - 1):
        mem[i][i + 1] = (s[i] == s[i + 1])

    for k in range(3, n + 1):
        for start in range(0, n - k + 1):
            end = start + k - 1
            mem[start][end] = s[start] == s[end] and mem[start + 1][end - 1]

    max_len = 0
    start = end = 0
    for i in range(0, n):
        for j in range(0, n):
            if mem[i][j] and (j - i + 1) > max_len:
                max_len = j - i + 1
                start = i
                end = j

    return s[start:start + max_len]


print longestPalindrome("abababba")
print longestPalindrome_dp("abababba")
