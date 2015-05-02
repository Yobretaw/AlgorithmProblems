import sys
import math
from collections import defaultdict

"""
    Given an array of strings, return all groups of strings that are anagrams.

    Note: All inputs will be in lower-case.
"""
def anagrams(strs):
        n = len(strs)

        if n < 2:
            return []

        strs.sort()

        m = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted([c for c in s]))
            m[sorted_s].append(s)

        res = []
        for key, val in m.iteritems():
            if len(val) > 1:
                res.extend(val)

        return res


