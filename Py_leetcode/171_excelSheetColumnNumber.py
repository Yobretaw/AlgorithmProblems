import sys
import math

"""
    Related to question Excel Sheet Column Title

    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
"""
def title_to_number(s):
    if not s:
        return 0

    res = 0
    for c in s:
        res = 26 * res + ord(c) - ord('A') + 1
    return res

#print title_to_number('AAA')
