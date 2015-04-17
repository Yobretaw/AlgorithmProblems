import sys
import os
import math

"""
    ============================================================================================
    Design a stack that supports a 'max' operation, which returns the maximum value stored in
    the stack.
    ============================================================================================
"""
class MaxStack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        curr_max = self.stack[-1][1] if len(self.stack) else -sys.maxint
        if val > curr_max:
            val = (val, val)
        else:
            val = (val, curr_max)

        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]
    
    def get_max(self):
        return self.stack[-1][1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0



#s = MaxStack()
#for i in range(0, 100):
#    s.push(i)

#for i in range(0, 100):
#    print s.get_max()
#    s.pop()
