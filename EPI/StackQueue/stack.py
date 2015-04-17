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
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]
    
    def get_max(self):
        return self.stack[-1][1]

    def __repr__(self):
        return [a[0] for a in self.stack]

    def empty(self):
        return len(self.stack) == 0

    def to_array(self):
        return [i[0] for i in self.stack]

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.queue:
            return None
        else:
            return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

    def push(self, val):
        self.queue.insert(0, val)

    def inject(self, val):
        self.enqueue(val)

    def pop(self):
        return self.dequeue()

    def eject(self):
        return self.queue.pop()

    def to_array(self):
        return [a for a in self.queue]

    def __repr__(self):
        return str(self.to_array())
