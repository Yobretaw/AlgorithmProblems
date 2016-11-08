import sys
import os
import math

from stack import Stack

"""
    ============================================================================================
    Problem 9.3 defines matched strings of parens, brackets and braces. This problem is restricted
    to strings of parens. Specifically, this problem is concerned with a long substrings of matched
    parens. As a example, if s is '((())()(()(', then '(())()' is the longest substring of matched
    parens.

    Write a function that takes as input a string made up of the characters '(' and ')', and returns
    the size of a maximum length substring in which the parens are matched.
    ============================================================================================
"""
def longest_matched_parens(s):
        if not s:
            return 0

        n = len(s)
        opens = Stack()
        max_len = 0
        start = 0
        for i in range(0, n):
            c = s[i]
            if c == '(':
                opens.push(i)
            elif opens.empty():
                start = i + 1
            else:
                opens.pop()
                if not opens.empty():
                    l = i - opens.top()
                else:
                    l = i - start + 1
                
                max_len = max(max_len, l)

        return max_len


#print longest_matched_parens('((())()(()(')
#print longest_matched_parens('()()()()()((()))(')
#print longest_matched_parens(')()())()()(')
#print longest_matched_parens('(()))())(')
#print longest_matched_parens('(()')
