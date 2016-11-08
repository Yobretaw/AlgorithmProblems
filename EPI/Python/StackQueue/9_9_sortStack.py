import sys
import os
import math
import imp

from stack import Stack

"""
    ============================================================================================
    Design an algorithm to sort a stack in descending order, i.e., the top of the stack holds
    the largest value. The only operations allowed are 'push', 'pop', 'top', and 'empty'. You
    cannot explicitly allocate memory outside of a few words.
    ============================================================================================
"""
def stack_sort(s):
    if not s.empty():
        e = s.top()
        s.pop()
        stack_sort(s)
        stack_insert(s, e)

def stack_insert(s, e):
    if s.empty() or s.top() <= e:
        s.push(e)
    else:
        f = s.top()
        s.pop()
        stack_insert(s, e)
        s.push(f)


s = Stack()
for i in reversed(range(0, 100)):
    s.push(i)

stack_sort(s)
print s.to_array()
