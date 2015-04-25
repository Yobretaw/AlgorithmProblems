import sys
import math
from collections import defaultdict

"""
    Implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") -> false
    isMatch("aa","aa") -> true
    isMatch("aaa","aa") -> false
    isMatch("aa", "*") -> true
    isMatch("aa", "a*") -> true
    isMatch("ab", "?*") -> true
    isMatch("aab", "c*a*b") -> false
"""
m = {}
def wildcard_matching(s, p):
    if m.has_key((s, p)): return m[(s, p)]
    if not s:
        if p and p[0] == '*':
            m[(s, p)] = wildcard_matching(s, p[1:])
            return m[(s, p)]
        else:
            return p == ""
    
    if not p:
        return False

    if p[0] == '?':
        m[(s, p)] = wildcard_matching(s[1:], p[1:])
        return m[(s, p)]
    elif p[0] == '*':
        j = 0
        while j < len(p) and p[j] == '*':
            j += 1
        for i in range(0, len(s)):
            m[(s, p)] = wildcard_matching(s[i + 1:], p[j:])
            if m[(s, p)]:
                return True
        m[(s, p)] = False
        return False
    else:
        m[(s, p)] = p[0] == s[0] and wildcard_matching(s[1:], p[1:])
        return m[(s, p)]


def wildcard_matching2(s, p):
    m = len(s)
    n = len(p)

    i = 0
    j = 0
    j_star = -1
    si = 0
    while i < m:
        if j < n and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < n and p[j] == '*':
            j_star = j
            si = i
            j += 1
        elif j_star >= 0:
            i = si + 1
            si += 1
            j = j_star + 1
        else:
            return False

    if i < m:
        return False

    while j < n and p[j] == '*':
        j += 1

    return j == n

    

#print wildcard_matching2("aa","a")
#print wildcard_matching2("aa","aa")
#print wildcard_matching2("aaa","aa")
#print wildcard_matching2("aa", "*")
#print wildcard_matching2("aa", "a*")
#print wildcard_matching2("ab", "?*")
#print wildcard_matching2("aab", "c*a*b")
#print wildcard_matching2("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b")
#print wildcard_matching2("abbbaaaaaaaabbbabaaabbabbbaabaabbbbaabaabbabaabbabbaabbbaabaabbabaabaabbbbaabbbaabaaababbbbabaaababbaaa", "ab**b*bb*ab**ab***b*abaa**b*a*aaa**bba*aa*a*abb*a*a")
#print wildcard_matching2("abaabababbbababbbababaaababbaaabbabaaabbbaaabbbaaabbabbababbababbbabbbaabaaaaabaaabbbbbabababababbbbabbaaaaaabaabbbaaaaaaaababbbbaabaabaaaaabaabbabaaaabaaaababaaaaaabaabaabaaaaababbaabaabbababbabbbabb", "ab*bbab*bb*b****ba*ab*ba*aba**b***aa*b*a*bbbaaa*a**bb*b*****aab**b*****a*abaab*a*aba**a*a*aaab*****abba")
#print wildcard_matching2("abefcdgiescdfimde", "ab*cd?i*de")
