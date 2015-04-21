import sys
import math
import imp

"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    "((()))", "(()())", "(())()", "()(())", "()()()"
"""
def generate_parentheses(n):
    res = []
    generate_parentheses_help("", 0, n, res)
    return res

    def generate_parentheses_help(curr, open_count, n, res):
        if len(curr) == 2 * n:
            res.append(curr)
            return

        if open_count < n:
            generate_parentheses_help(curr + '(', open_count + 1, n, res)

        if open_count > (len(curr) - open_count):
            generate_parentheses_help(curr + ')', open_count, n, res)

print generate_parentheses(3)
