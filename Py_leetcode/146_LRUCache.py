import sys
import math
import imp
from collections import defaultdict, deque, OrderedDict

"""
    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
    following operations: get and set.

        - get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise
          return -1.

        - set(key, value) - Set or insert the value if the key is not already present. When the cache reached its
          capacity, it should invalidate the least recently used item before inserting a new item.
"""
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.m = OrderedDict()

    def get(self, key):
        if not key in self.m:
            return -1
        else:
            val = self.m[key]
            self.m.pop(key, None)
            self.m[key] = val
            return val

    def set(self, key ,val):
        if not key in self.m:
            if len(self.m) == self.capacity:
                self.m.popitem(False)
            self.m[key] = val
        else:
            self.m.pop(key, None)
            self.m[key] = val

    #def __init__(self, capacity):
    #    self.capacity = capacity
    #    self.q = []
    #    self.m = {}

    ## @return an integer
    #def get(self, key):
    #    if key in self.m:
    #        self.q.remove(key)
    #        self.q.append(key)
    #        return self.m[key]
    #    else:
    #        return -1

    ## @param key, an integer
    ## @param value, an integer
    ## @return nothing
    #def set(self, key, value):
    #    if not key in self.m:
    #        if len(self.q) == self.capacity:
    #            self.m.pop(self.q[0], None)
    #            self.q.remove(self.q[0])
    #        self.m[key] = value
    #        self.q.append(key)
    #    else:
    #        self.m[key] = value
    #        self.q.remove(key)
    #        self.q.append(key)

#c = LRUCache(2)
#c.set(2,1)
#c.set(1,1)
#c.set(2,3)
#c.set(4,1)
#print c.get(1)
#print c.get(2)

# ------------

#c.set(2, 1)
#c.set(1, 1)
#print c.get(2)
#c.set(4, 1)
#print c.get(1)
#print c.get(2)
