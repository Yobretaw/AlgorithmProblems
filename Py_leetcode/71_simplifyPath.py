import sys
import os
import math

"""
    Given an absolute path for a file (Unix-style), simplify it.

    For example,
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"

    Corner Cases:

    Did you consider the case where path = "/../"?

    In this case, you should return "/".

    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
"""
def simplify_path(s):
    if not s:
        return s

    st = []
    s = [c for c in s.split('/') if c]
    for part in s:
        if part == '.':
            continue
        elif part == '..':
            if len(st) > 0:
                st.pop()
        else:
            st.append(part)

    return '/' + '/'.join(st)


#print simplify_path('/home/')
#print simplify_path('/a/./b/../../c/')
#print simplify_path('/../')
#print simplify_path('/home//foo/')
