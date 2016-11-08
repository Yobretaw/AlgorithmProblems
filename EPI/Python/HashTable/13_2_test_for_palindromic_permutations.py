import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a program to test whether the letters forming a string can be permuted
    to form a palindrome. For example, "edified" can be permuted to from "deified"

    ===========

    Such permutation exists if and only if the number of odd occurences of characters
    is less than 2
"""
def test_form_palindrome(s):
    n = len(s)
    if n < 2:
        return True

    c = Counter(s)
    odd_count = 0
    for k, v in c.iteritems():
        if v % 2 == 1 and odd_count:
            return False
        elif v % 2 == 1:
            odd_count += 1
    return True

print test_form_palindrome('edifiedee')
#print test_form_palindrome('edified')
