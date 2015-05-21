import sys
import math
from sets import Set

"""
    All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When
    studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

    Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

    For example,

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

    Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].
"""
def find_repeated_sequence(s):
    n = len(s)
    if n < 11:
        return []

    res = []
    seen = {}
    seen[s[:10]] = 0
    for i in range(1, n - 9):
        curr = s[i:i + 10]
        if not curr in seen:
            seen[curr] = 0
        elif seen[curr] == 0:
            res.append(curr)
            seen[curr] += 1
    return res

def find_repeated_sequence2(s):
    n = len(s)
    if n < 11:
        return []
    
    charToNum = {
        'A': 1,
        'T': 2,
        'G': 3,
        'C': 4
    }

    val = 0
    for i in range(0, 10):
        val = 10 * val + charToNum[s[i]]

    res = []
    seen = {}
    seen[val] = 1
    power = 10 ** 9
    for i in range(1, n - 9):
        val %= power
        val = 10 * val + charToNum[s[i + 9]]
        if not val in seen:
            seen[val] = 1
        elif seen[val] == 1:
            res.append(s[i:i + 10])
            seen[val] += 1
    return res

#print find_repeated_sequence("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
#print find_repeated_sequence2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
