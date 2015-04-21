import sys
import math

"""
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
def is_valid(s):
    n = len(s)

    if n & 1:
        return False

    st = []
    for c in s:
        if c in ['(', '[', '{']:
            st.append(c)
        elif len(s) == 0:
            return False
        else:
            if not is_valid_pair(st[-1] + c):
                return False
            st.pop()
    return True


def is_valid_pair(s):
    return s in ['()', '[]', '{}']


#l = '()'
#print is_valid(l)

#l = '()[]{}'
#print is_valid(l)

#l = '(]'
#print is_valid(l)

#l = '([)]'
#print is_valid(l)
