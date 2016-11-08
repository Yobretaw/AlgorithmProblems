import sys
import os
import math


"""
    Implement a method that takes as input a set S of n distinct elements, and
    prints the power set of S. Print the subsets one per line, with elements
    separated by commas.
"""
def enumerate_power_set(s):
    if not s:
        return
    
    s = list(s)
    enumerate_power_set_help(s, 0, [])


def enumerate_power_set_help(s, idx, curr):
    if idx == len(s):
        print curr
        return

    enumerate_power_set_help(s, idx + 1, curr)
    curr.append(s[idx])
    enumerate_power_set_help(s, idx + 1, curr)
    curr.pop()


"""
    Variant 16.5.1

    Solve the same problem when the input set may have duplicates, i.e., denotes
    as multiset. You should not repeat any multiset.
"""
def enumerate_power_set_dup(s):
    if not s:
        return

    s = sorted(list(s))
    seen = set()
    enumerate_power_set_dup_help(s, 0, [], seen)

def enumerate_power_set_dup_help(s, idx, curr, seen):
    if idx == len(s):
        print curr
        return

    next_idx = idx + 1
    while next_idx < len(s) and s[idx] == s[next_idx]:
        next_idx += 1

    enumerate_power_set_dup_help(s, next_idx, curr, seen)
    for i in range(idx, next_idx):
        curr.append(s[i])
        enumerate_power_set_dup_help(s, next_idx, curr, seen)

    curr[:] = curr[:-(next_idx - idx)]


if __name__ == '__main__':
    enumerate_power_set([1, 2, 3, 4, 5])
    enumerate_power_set_dup([1, 2, 3, 4, 5, 1])
