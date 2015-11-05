import sys
import os
import math


"""
    You are given n rings. The i-th ring has diamter i. The rings are initially
    in sorted order on a peg(P1), with the largest ring at the bottom. You are
    to transfer these rings to another peg(P2), which is initially empty. You
    have a third peg(P3), which is initially empty. The only operation you can
    do is taking a single ring from the top of one peg and placing it on the top
    of another peg; you must never place a bigger ring above a smaller ring.

    Exactly n rings on P1 peg need to be transferred to P2, possibly using P3
    as an intermediate, subject to the stacking constraint. Write a function
    that prints a sequence of operations that transfers all rings from P1 to
    P3.
"""
def transfer(n):
    transfer_help(n, 0, 1, 2)

def transfer_help(n, from_peg, to_peg, intermediate_peg):
    if n <= 0:
        return

    transfer_help(n - 1, from_peg, intermediate_peg, to_peg)
    print 'Move ring %s from peg %s to peg %s' % (str(n), str(from_peg), str(to_peg))
    transfer_help(n - 1, intermediate_peg, to_peg, from_peg)


if __name__ == '__main__':
    transfer(5)
