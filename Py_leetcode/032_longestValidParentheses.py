import sys
import math

"""
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    For "(()", the longest valid parentheses substring is "()", which has length = 2.

    Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
def longest_valid_parentheses(s):
        if not s or len(s) < 2:
            return 0

        # stack
        st = []
        
        # every when st gets empty, we update start_pos
        start_pos = 0
        max_len = 0

        n = len(s)
        for i in range(0, n):
            if s[i] == '(':
                st.append(i)
            elif not st:
                start_pos = i + 1
            else:
                st.pop()
                if not st:
                    max_len = max(max_len, i - start_pos + 1)
                else:
                    max_len = max(max_len, i - st[-1])

        return max_len

# Space: O(1)
def longest_valid_parentheses2(s):
        if not s or len(s) == 1:
            return 0

        n = len(s)

        depth = 0
        start = 0
        max_len = 0
        for i in range(0, n):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = i + 1
                    depth = 0
                elif depth == 0:
                    max_len = max(max_len, i - start + 1)

        start = n - 1
        depth = 0
        for i in reversed(range(0, n)):
            if s[i] == ')':
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = i - 1
                    depth = 0
                elif depth == 0:
                    max_len = max(max_len, start - i + 1)

        return max_len


#s = ')()())'
#print longest_valid_parentheses(s)
#print longest_valid_parentheses2(s)

#s = ')()()())'
#print longest_valid_parentheses(s)
#print longest_valid_parentheses2(s)

#s = '(()'
#print longest_valid_parentheses(s)
#print longest_valid_parentheses2(s)
