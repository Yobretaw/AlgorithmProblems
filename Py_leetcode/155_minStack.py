import sys
import os
import math

"""
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

     - push(x) -- Push element x onto stack.
     - pop() -- Removes the element on top of the stack.
     - top() -- Get the top element.
     - getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack:
    def __init__():
        self.l = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        min_val = x if not self.l or x < self.l[-1][1] else self.l[-1][1]
        self.l.append((x, min_val))

    # @return nothing
    def pop(self):
        res = self.l[-1]
        self.l.pop()
        return res
        

    # @return an integer
    def top(self):
        return self.l[-1][0]
        

    # @return an integer
    def getMin(self):
        return self.l[-1][1]


class MinStack2:
    def __init__(self):
        self.l = []
        self.min_val = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.l:
            self.min_val = x
            self.l.append(0)
        else:
            self.l.append(x - self.min_val)
            self.min_val = min(self.min_val, x)

    # @return nothing
    def pop(self):
        if not self.l:
            return
        val = self.l[-1]
        self.l.pop()

        if val < 0:
            self.min_val -= val

    # @return an integer
    def top(self):
        top = self.l[-1]
        if top > 0:
            return top + self.min_val
        else:
            return self.min_val

    # @return an integer
    def getMin(self):
        return self.min_val

#st = MinStack2()
#st.push(2)
#st.push(0)
#st.push(3)
#st.push(0)
#print st.getMin()
#st.pop()
#print st.getMin()
#st.pop()
#print st.getMin()
#st.pop()
#print st.getMin()
