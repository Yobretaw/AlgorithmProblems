import sys
import math
from itertools import izip_longest
"""
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.
    The . character does not represent a decimal point and is used to separate number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level
    revision of the second first-level revision.

    Here is an example of version numbers ordering:

    0.1 < 1.1 < 1.2 < 13.37
"""
def compare_version(v1, v2):
    v1 = [int(c) for c in v1.split('.')]
    v2 = [int(c) for c in v2.split('.')]
    for n1, n2 in izip_longest(v1, v2, fillvalue=0):
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
    return 0
    
    #m, n = len(v1), len(v2)
    #for i in range(0, min(m, n)):
    #    if v1[i] < v2[i]:
    #        return -1
    #    elif v1[i] > v2[i]:
    #        return 1
    
    #rest = v1 if m > n else v2
    #idx = n if m > n else m
    #sign = 1 if m > n else -1
    #while idx < len(rest):
    #    if rest[idx] != 0:
    #        return sign
    #    idx += 1
    #return 0

#print compare_version('1.0.0.1', '1')
#print compare_version('1.1', '1.01')
