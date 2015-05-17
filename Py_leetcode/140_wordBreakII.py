import sys
import math

"""
    Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
    where each word is a valid dictionary word.

    Return all such possible sentences.

    For example, given
    s = "catsanddog",
    dict = ["cat", "cats", "and", "sand", "dog"].

    A solution is ["cats and dog", "cat sand dog"].
"""
def word_break(s, d):
    if not s:
        return []

    res = []
    mem = {}
    dfs(s, d, res, '', mem)
    return res


def dfs(s, d, res, curr, mem):
    if not s:
        res.append(curr.strip())
        return True

    if s in mem:
        return False
    
    ret = False
    for i in range(1, len(s) + 1):
        if s[:i] in d:
            if dfs(s[i:], d, res, curr + ' ' + s[:i], mem):
                ret = True
    if not ret: mem[s] = False
    return ret


#s = "catsanddog"
#d = ["cat", "cats", "and", "sand", "dog"]
#for line in word_break(s, d):
#    print line
