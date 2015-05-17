import sys
import math

"""
    Given a string s and a dictionary of words dict, determine if s can be segmented into a
    space-separated sequence of one or more dictionary words.

    For example, given
    s = "leetcode",
    dict = ["leet", "code"].

    Return true because "leetcode" can be segmented as "leet code".
"""
def word_break(s, d):
    if not s:
        return s in d

    if s in d:
        return True

    return dfs(s, d, 0, {})

def dfs(s, d, idx, mem):
    if idx == len(s):
        return True

    if s[idx:] in mem:
        return mem[s[idx:]]

    for i in range(idx + 1, len(s) + 1):
        if s[idx:i] in d:
            if dfs(s, d, i, mem):
                mem[s[idx:]] = 1
                return True

    mem[s[idx:]] = 0
    return False


def word_break_iterative(s, d):
    if not s:
        return s in d
    
    if s in d:
        return True
    
    n = len(s)
    f = [0] * (n + 1)
    for i in range(0, n + 1):
        f[i] = s[:i] in d
    for i in range(0, n + 1):
        for j in range(i, n + 1):
            f[j] |= f[i] and s[i:j] in d
    return f[-1]


#s = 'leetcode'
#d = ['leet', 'code']

#s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
#d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#print word_break_iterative(s, d)
