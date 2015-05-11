import sys
import os
import math

"""
    Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

    Below is one possible representation of s1 = "great":

        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t

    To scramble the string, we may choose any non-leaf node and swap its two children.

    For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t

    We say that "rgeat" is a scrambled string of "great".

    Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a

    We say that "rgtae" is a scrambled string of "great".

    Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
def is_scramble(s1, s2):
    m = {}
    return f(s1, s2, m)


def f(s1, s2, m):
    if (s1, s2) in m:
        return m[(s1, s2)]

    if not s1 and not s2:
        return True
    elif len(s1) == 1 and len(s2) == 1:
        return s1 == s2
    elif not sorted(s1) == sorted(s2):
        return False

    for i in range(1, len(s1)):
        if f(s1[:i], s2[-i:], m) and f(s1[i:], s2[:-i], m) or \
           f(s1[:i], s2[:i], m) and f(s1[i:], s2[i:], m):
            m[(s1, s2)] = True
            return True
    m[(s1, s2)] = False
    return False

#print is_scramble('great', 'rgeat')
#print is_scramble('great', 'rgtae')
#print is_scramble('abcdefghijklmnopq', 'efghijklmnopqcadb')
