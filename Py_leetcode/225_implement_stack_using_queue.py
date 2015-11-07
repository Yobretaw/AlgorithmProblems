import sys

"""
    Implement the following operations of a stack using queues.

        push(x) -- Push element x onto stack

        pop() -- Removes the element on the top of the stack.

        top() -- Get the top element

        empty() -- Return whether the stack is empty
        

    You must use only standard operations of a queue -- which means only

        'push_to_back', 'peek/pop from front', 'size' and 'is_empty'

    are valid operations.
"""
class Stack(object):
    def __init__(self):
        self.q = []

    def push(self, x):
        tmp = [x]
        while self.q:
            tmp.append(self.q.pop(0))
        self.q = tmp

    def pop(self):
        self.q.pop(0)

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


if __name__ == '__main__':
    s = Stack()
    for i in range(1, 10):
        s.push(i)

    for i in range(1, 10):
        print s.top()
        s.pop()
