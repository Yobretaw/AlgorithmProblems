import os
import math
import sys
from collections import defaultdict, Counter
from heapq import *

"""
    You are given a log file containing search queries. Each query is a string,
    and queries are separated by newlines. Diverse applications, such as auto-
    completion and trend analysis, require computing the most frequent queries.
    In the abstract, you are to solve the following problem.

    Given an array of strings, compute the k strings that appear most frequently
    in the array.
"""
def compute_k_most_frequence_strings(arr, k):
    """
        Brute-force algorithm
    """
    if len(arr) < k:
        return arr

    c = Counter(arr)
    return c.most_common(k)

def compute_k_most_frequence_strings_2(arr, k):
    """
        Use heap
    """
    if len(arr) < k:
        return arr

    d = defaultdict(int)

    idx = 0
    while len(d) < k and idx < len(arr):
        d[arr[idx]] += 1
        idx += 1

    h = [None] * k
    j = 0
    for k, v in d.iteritems():
        h[j] = (v, k)
        j += 1

    heapify(h)
    appeared_key = {}
    for v in h:
        appeared_key[v[1]] = 1
    for i in range(idx, len(arr)):
        d[arr[i]] += 1
        if d[arr[i]] > h[0][0] and not arr[i] in appeared_key:
            appeared_key.pop(heappop(h)[1])
            heappush(h, (d[arr[i]], arr[i]))
            appeared_key[arr[i]] = 1
    res = []
    for v in h:
        res.append((v[1], d[v[1]]))
    return res[::-1]


s = """
    You are given a log file containing search queries. Each query is a string,
    and queries are separated by newlines. Diverse applications, such as auto-
    completion and trend analysis, require computing the most frequent queries.
    In the abstract, you are to solve the following problem.

    Given an array of strings, compute the k strings that appear most frequently
    in the array.
"""
s = s.replace(',', '')
s = s.replace('.', '')
print compute_k_most_frequence_strings(s.split(), 3)
print compute_k_most_frequence_strings_2(s.split(), 3)
