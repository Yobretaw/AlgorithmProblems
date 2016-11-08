import sys
import os
import math
import imp

from stack import Stack

"""
    ============================================================================================
    Queue insertion and deletion follows FIFO semantics; stack insertion and deletion is LIFO.

    Implement a queue given a library implemention of stack.
    ============================================================================================
"""
class MyQueue():
    def __init__(self):
        self._in = Stack()
        self._out = Stack()
        self.count = 0

    def enqueue(self, val):
        self._in.push(val)
        self.count += 1

    def dequeue(self):
        if self._out.empty():
            while not self._in.empty():
                self._out.push(self._in.top())
                self._in.pop()

        res = self._out.top()
        self._out.pop()
        self.count -= 1

        return res

    def size(self):
        return self.count


    def empty(self):
        return self.size() == 0



q = MyQueue()
for i in range(0, 10):
    q.enqueue(i)

for i in range(0, 5):
    q.dequeue()

for i in range(0, 10):
    q.enqueue(i)

for i in range(0, q.size()):
    print q.dequeue()
