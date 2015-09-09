import sys
import os
import math
import imp
import random

"""
    Design an algorithm that takes a sorted array whose length is not known,
    and a key, and returns an index of an array element which is equal to the
    key. Assume that an out-of-bounds access throws an exception.
"""
class MyList(list):
    def at(self, idx):
        if idx >= len(self):
            raise Exception('Invalid Index')
        return self[idx]

def search_sorted_array_of_unknown_length(arr, k):
    p = 0
    while True:
        try:
            idx = (1 << p) - 1
            if arr.at(idx) == k:
                return idx
            elif arr.at(idx) > k:
                break
        except Exception:
            break
        p += 1

    # binary search between indices 2^(p - 1) and 2^p - 2
    l, r = 1 << (p - 1), (1 << p) - 1
    while l <= r:
        mid = l + (r - l) / 2
        try:
            if arr.at(mid) == k:
                return k
            elif arr.at(mid) > k:
                r = mid
            else:
                l = mid + 1
        except Exception:
            r = mid

    return -1

#def search_sorted_array_of_unknown_length(l, k):
#    i = 1
#    while True:
#        try:
#            v = l.at(i)
#            if v == k:
#                return i
#            elif v < k:
#                i *= 2
#            else:
#                return binary_search(l, k)
#        except Exception:
#            i -= 1
#    return -1

#def binary_search(arr, k):
#    n = len(arr)
#    if not n:
#        return -1

#    l, r = 0, n
#    while l < r:
#        mid = l + (r - l) / 2
#        if arr.at(mid) == k:
#            return mid
#        elif arr.at(mid) > k:
#            r = mid
#        else:
#            l = mid + 1
#    return -1


l = MyList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(len(l)):
    print search_sorted_array_of_unknown_length(l, i)
