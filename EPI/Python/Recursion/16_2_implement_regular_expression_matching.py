import sys
import os
import math


"""
    ESRS(Extended Simple Regular Expression) contains a sequence of
    
        1. Alphanumeric character that matches itself

        2. '.' that matches any single character

        3. '*' that matches zero or more occurences of the preceding regular
        expressions.

        4. '^' indicates the match must begin at the start of the string

        5. '$' indicates the match must end at the end of the string.

    If the given RSRE r does not contain '^' and '$', the r matches s if there
    is a substring t of s such that r strictly matches t.

    Design an algorithm that takes a string s and a string r, assumed to be a
    well-formed ESRE, and checks if r matches s.
"""
def match(s, r):
    seen = {}
    if r and r[0] == '^':
        return match_help(s, r[1:], seen)
    else:
        for i in range(0, len(r)+1):
            if match_help(s, r[i:], seen):
                return True
    return False


def match_help(s, r, seen):
    key = (s, r)

    #print key
    if key in seen:
        return seen[(s, r)]

    if not s:
        return not r or r[-1] != '$' or r.replace('.*', '').replace('*', '') == '$'

    if not r:
        return s == ''
    
    if r[0] == '^':
        seen[key] = match_help(s, r[1:], seen)
        return seen[key]

    if not s[0] == r[0] and r[0] != '.':
        seen[key] = False
        return seen[key]

    if len(r) <= 1 or r[1] != '*':
        seen[key] = match_help(s[1:], r[1:], seen)
        return seen[key]

    if len(r) > 1 and r[1] == '*':
        for i in range(0, len(s)):
            if (r[0] == '.') and match_help(s[i:], r[2:], seen) or \
                    s[i] == s[0] and match_help(s[i+1:], r[2:], seen):
                seen[key] = True
                return seen[key]

    seen[key] = False
    return seen[key]


if __name__ == '__main__':
    print match('', '') == True
    print match('', '.*') == True
    print match('', '^.*') == True
    print match('', '.*$') == True
    print match('', '^.*$') == True
    print match('a', '^.*$') == True
    print match('aaa', '^.*$') == True
    print match('aaa', '^a*$') == True

    print match('abc', 'abc') == True
    print match('abc', 'abc$') == True
    print match('abc', '^abc') == True
    print match('abc', '^abc$') == True

    print match('abc', '^abc.*') == True
    print match('abc', '.*abc.*') == True
    print match('abc', '.*a.c.*') == True
    print match('abc', '.*a.*c.*') == True

    print match('abc', 'ab*c') == True
    print match('abc', 'a*b*c*') == True

    print match('abc', 'aaaa*b*c*') == True
    print match('abc', '^aaaa*b*c*') == False

    print match('abc', 'aaaa*b*c*jflks') == True
    print match('abc', 'aaaa*b*c*jflk$') == False
