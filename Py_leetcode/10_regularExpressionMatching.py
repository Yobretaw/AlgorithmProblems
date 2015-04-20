import sys
import math

"""
    Implement regular expression matching with support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:

    isMatch("aa","a") -> false
    isMatch("aa","aa") -> true
    isMatch("aaa","aa") -> false
    isMatch("aa", "a*") -> true
    isMatch("aa", ".*") -> true
    isMatch("ab", ".*") -> true
    isMatch("aab", "c*a*b") -> true
"""
def is_match(s, p):
    cache = {}
    return is_match_help(s, p, cache)

    
def is_match_help(s, p, cache):
    if (s, p) in cache:
        return cache.get((s, p))

    if p == "":
        cache[(s, p)] = s == ""
        return s == ""

    if len(p) == 1 or p[1] != '*':
        cache[(s, p)] = s != "" and (p[0] == s[0] or p[0] == '.') and is_match_help(s[1:], p[1:], cache)
        return cache[(s, p)]

    i = 0
    while i < len(s) and (p[0] == '.' or s[i] == p[0]):
        if is_match_help(s[i:], p[2:], cache):
            cache[(s, p)] = True
            return True
        i += 1

    cache[(s, p)] = is_match_help(s[i:], p[2:], cache)
    return cache[(s, p)]


#print is_match("", "")
#print is_match("a", "a")
#print is_match("aa", "aa")
#print is_match("aa", "a*")
#print is_match("aa", ".*")
#print is_match("ab", ".*")
#print is_match("aab", "c*a*b")
#print is_match("aab", "c*a*b*")
#print is_match("aab", "c*a*b.*")

#print '-' * 100

#print is_match("a", "")
#print is_match("", "a")
#print is_match("aa", "aaa")
#print is_match("aa", "a")
#print is_match("aaa", "aa")
#print is_match("aaa", "aab")
#print is_match("aaa", "aaab")
