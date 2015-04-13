import sys
import os
import math

class Stack():
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
        return self.stack.pop()

    def top(self):
        return self.stack[-1][0]
    
    def get_max(self):
        return self.stack[-1][1]

    def __repr__(self):
        print [a[0] for a in self.stack]

    def empty(self):
        return len(self.stack) == 0

    def to_array(self):
        return [i[0] for i in self.stack]
