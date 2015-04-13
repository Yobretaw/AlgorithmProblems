import sys
import os
import math

from stack import Stack

"""
    ============================================================================================
    A string over "{,},(,),[,]" is said to be well-formed if the different types of brackets
    match in the correct order.

    Write a function that tests if a string made up of the characters '(', ')', '[', ']', '{', '}'
    is well-formed.
    ============================================================================================
"""
def is_well_formed(t):
    if not t:
        return True

    n = len(t)

    if n & 1:
        return False
    
    s = Stack()
    for c in t:
        if c == '{' or c == '(' or c == '[':
            s.push(c)
        elif s.empty():
            return False
        else:
            if not match(s.top() + c):
                return False
            else:
                s.pop()

    return s.empty()


def match(pair):
    return pair in ['()', '[]', '{}']


#print is_well_formed(')')
#print is_well_formed('([]){()}')
#print is_well_formed('[()[]{()()}]')
#print is_well_formed('{)')
#print is_well_formed('[()[]{()()')
