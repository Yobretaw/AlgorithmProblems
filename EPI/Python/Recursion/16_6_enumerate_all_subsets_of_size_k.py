import sys
import os
import math


"""
    Write a function that takes as input integers n and k, and computes all
    subsets of size k of the set {1, 2, ..., n}
"""
def enumerate_k_size_subset(n, k):
    s = [i + 1 for i in range(n)]
    enumerate_k_size_subset_help(s, k, 0, [])

def enumerate_k_size_subset_help(s, k, idx, curr):
    if idx == len(s):
        if len(curr) == k:
            print curr
        return

    enumerate_k_size_subset_help(s, k, idx + 1, curr)
    curr.append(s[idx])
    enumerate_k_size_subset_help(s, k, idx + 1, curr)
    curr.pop()


if __name__ == '__main__':
    enumerate_k_size_subset(6, 3)
