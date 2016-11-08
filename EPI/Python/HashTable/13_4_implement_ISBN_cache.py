import os
import math
import sys
from collections import defaultdict, Counter, OrderedDict

"""
    Implement a cache for looking up prices of books identified by their ISBN.
    You should support lookup, insert, and erase methods. use the Least Recent
    Used(LRU) strategy for cache evicition policy.
"""
class ISBN_Cache():
    def __init__(self):
        self.cache = OrderedDict()
        self.cache_size = 100

    def insert(self, key, val):
        if val in self.cache:
            self.cache.pop(key)
            self.cache[key] = val
        else:
            if len(self.size) > self.cache:
                self.cache.popitem(last=False)
            self.cache[key] = val

    def lookup(self, key, val):
        if key in self.cache:
            return self.cache[key]
        return None

    def erase(self, key):
        if key in self.cache:
            self.cache.pop(key)

