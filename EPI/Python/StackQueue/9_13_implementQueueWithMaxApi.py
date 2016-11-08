import sys
import os
import math
import imp

from stack import Stack
MaxStack = imp.load_source('MaxStack', './9_1_stackWithMaxApi.py').MaxStack

"""
    ============================================================================================
    A queue implements 'enqueue' and 'dequeue' operations. Suppose the keys are from a totally
    ordered set, e.g., integers, and we want to support a 'max' operation, which returns the
    maximum element stored in the queue.

    Implement a queue with 'enqueue', 'dequeue' and 'max' operations.
    ============================================================================================
"""
class MaxQueue():
    def __init__(self):
        self._in = MaxStack()
        self._out = MaxStack()

    def enqueue(self, val):
        self._in.push(val)

    def dequeue(self):
        if self._out.empty():
            while not self._in.empty():
                self._out.push(self._in.top())
                self._in.pop()
        
        res = self._out.top()
        self._out.pop()
        return res

    def max(self):
        in_max = self._in.get_max() if not self._in.empty() else -sys.maxint
        out_max = self._out.get_max() if not self._out.empty() else -sys.maxint
        return max(in_max, out_max)

    def size(self):
        return self._in.size() + self._out.size()



#q = MaxQueue()

#a = [1.3, 0, 2.5, 3.7, 0, 1.4, 2.6, 0, 2.2, 1.7, 0, 0, 0, 0, 1.7]
#for i in range(0, 4):
#    q.enqueue(a[i])
#    print i, q.max()

#for i in range(4, len(a)):
#    q.dequeue()
#    q.enqueue(a[i])
#    print i, q.max()

#q.enqueue(3)
#q.enqueue(2)
#q.enqueue(1)
#q.enqueue(5)
#q.enqueue(4)
#q.enqueue(6)
#q.enqueue(7)
#q.enqueue(2)

#for i in range(0, q.size()):
#    print q.max()
#    q.dequeue()

