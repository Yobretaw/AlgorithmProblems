import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function that takes as input a set of words and returns groups of
    anagrams for those words
"""
def partition_anagrams(words):
    d = defaultdict(list)
    for w in words:
        s = ''.join(sorted(list(w)))
        d[s].append(w)
    
    res = [None] * len(d.keys())
    for i, x in enumerate(d.keys()):
        res[i] = d[x]

    return res

def partition_anagrams_2(words):
    d = defaultdict(list)
    for w in words:
        s = str(Counter(w))
        d[s].append(w)

    res = [None] * len(d.keys())
    for i, x in enumerate(d.keys()):
        res[i] = d[x]
    return res


#words = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis']
#print partition_anagrams_2(words)
