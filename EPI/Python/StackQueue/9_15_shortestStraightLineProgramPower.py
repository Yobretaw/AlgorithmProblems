import sys
import os
import math
import imp
from collections import deque

from stack import Stack
#MaxStack = imp.load_source('MaxStack', './9_1_stackWithMaxApi.py').MaxStack

"""
    ============================================================================================
    A straight-line program for computing x^n is a finite sequence <x, x^i_1, x^i_2, ..., x^i_n>
    where each element after the first is either the square of some previous element of the
    product of any two previous elements. For example, the term x^15 can be computed by the 
    following two straight-line program.

    P1 = <x, x^2= (x)^2, x^4 = (x^2)^2, x^8 = (x^4)^2, x^12 = x^8 * x^4, x^14 = x^12 * x^2, x^15 = x^14 * x
    p2 = <x, x^2 = (x)^2, x^3 = x^2 * x, x^5 = x^3 * x^2, x^10 = (x^5)^2, x^15 = x^10 * x^5

    Given a positive integer n, how would you compute a shortest straight-line program to evaluate
    x^n?

    ----------------------

    Here is a brute force approach: Compute all straight-line programs of length k, in increasing
    order of k. For k = 1, there is only one shortest straight-line program, namely <x>. We maintain
    a queue of straight-line programs ordered by length. We iteratively pop the queue. Suppose we
    are considering a length k straight-line program D. We try all combinations of elements in D
    to get length k + 1 straight-line programs, which we add to the back of the queue.

    Note that this process yields straight-line programs that are not necessarily optimum. However,
    since we are systematically exploring straigh-line programs in order of length, the first time
    we encounter a straight-line product yielding n, it must be a shortest straight-line program.

    Note the code implementation of this idea is essentially a BFS on the graph of all straight-line
    programs, where an edge exists from D to D' if D' is D followed by an element which derived
    from previous elements D.
    ============================================================================================
"""
def shortest_line_program2(n):
    if n == 1:
        return [1]

    q = deque()
    q.append([1])
    while len(q) > 0:
        candidate = q.popleft()

        # try all possbile combinations in candidate
        for a in candidate:
            power = a + candidate[-1]
            if power > n:
                # now possible for curr candidate
                break

            next_candidate = list(candidate)
            next_candidate.append(power)

            if power == n:
                return next_candidate

            q.append(next_candidate)

#print shortest_line_program2(15)

