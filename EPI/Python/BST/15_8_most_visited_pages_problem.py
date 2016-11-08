import sys
import os
import math
import imp

from collections import defaultdict
from BST import Node

quick_select = imp.load_source('Select', '../Util/quick_select.py').select


"""
    You are given a log file containing billions of entries. Each entry contains
    an integer 'timestamp' and 'page' which is of type string. The entries in a
    log file appear in increasing order of timestamp.

    You are to implement methods to analyze log file data to find the most visited
    pages. Specifically, implementing the following methods:

        - void add(Entry p)
        
        Add p.page to the set of visited pages. It is guaranteed that if add(q) is
        called after add(p), the q.timestamp >= p.timestamp.

        - List<String> common(k)

        Return a list of the k most common pages.


    First solve this problem when common(k) is called exactly once after all pages
    have been read. Then solve the problem when calls to 'common' and 'add' are
    interleaved. Assume you have unlimited RAM.
"""
class Analyzer:
    """
        Assume 'common' is called exactly once after all pages have been read.
    """
    def __init__(self):
        self.entries = defaultdict(int)

    def add(self, entry):
        _, page = entry
        self.entries[page] += 1

    def common(self, k):
        entries = list(self.entries)
        quick_select(entries, k - 1, lambda x: x[1])
        return entries[-k:]


#class AdvancedAnalyzer:
#    """
#        Assume call to 'add' and 'common' are interleaved.
#    """
#    def __init__(self):
#        self.page2Node = {}
