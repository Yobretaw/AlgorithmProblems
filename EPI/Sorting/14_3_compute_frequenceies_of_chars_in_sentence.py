import sys
import math
import itertools
import string
from collections import Counter


"""
    Given a string, print in alphabetical order each character that appears in
    the string, and the number of times that it appears. For example, if the 
    string is 'bcdacebe', print "(a, 1), (b, 2), (c, 2), (d, 1), (e, 2)".
"""
def print_freq_in_order(s):
    if not s:
        return

    counter = Counter(s)
    res = []
    for c in string.ascii_letters:
        if c in counter:
            res.append((c, counter[c]))
    print res


print_freq_in_order('bcdacebe')
