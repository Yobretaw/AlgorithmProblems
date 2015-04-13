import sys
import os
import math

from stack import Stack

"""
    ============================================================================================
    Write a function that takes an arithmetical expression in RPN and returns the number that
    the expression evaluates to.
    ============================================================================================
"""
def evaluate(exp):
    if not exp or len(exp) == 1:
        return 0 if not exp else int(exp)

    s = Stack()
    for c in exp.split(','):
        val = to_int(c)
        if val:
            s.push(val)
        else:
            a = s.top()
            s.pop()
            b = s.top()
            s.pop()
            s.push(eval(a, b, c))

    return s.top()


def to_int(a):
    try:
        return int(a)
    except ValueError:
        return None

def eval(a, b, op):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return ops[op](a, b)


#print evaluate('3,4,+,2,1,*,+')
#print evaluate('1,1,+,-2,*')


"""
    Variant 9.2.1: Solve the same problem for expression in Polish notation, i.e., when A, B, ? is 
    replaced by ? A, B.
"""
def polish_eval(exp):
    if not exp or len(exp) == 1:
        return 0 if not exp else int(exp)

    s = Stack()
    idx = 0
    exp = exp.split(',')
    for c in exp:
        val = to_int(c)
        if not val:
            s.push(c)
        elif isinstance(s.top(), int):
            prev = s.top()
            s.pop()
            op = s.top()
            s.pop()
            s.push(eval(prev, val, op))
        else:
            s.push(val)

    return s.top()

#print polish_eval("-,*,2,3,4")

