import sys
import os
import math
import imp
import random
import functools
from heapq import *

"""
    Implement a stack API using a heap

    Stack API:
        - push(v)
        - pop()
        - top()
"""
@functools.total_ordering
class FirstTuple(tuple):
    def __eq__(self, other):
        return self[0] == other[0]
    def __lt__(self, other):
        return self[0] < other[0]

class Stack():
    def __init__(self):
        self.h = []
        self.timestamp = 0

    def push(self, value):
        heappush(self.h, FirstTuple((-self.timestamp - 1, value)))
        self.timestamp += 1

    def pop(self):
        heappop(self.h)

    def top(self):
        return self.h[0][1]


#s = Stack()
#for i in range(100):
#    s.push(i)

#for i in range(100):
#    print s.top()
#    s.pop()
