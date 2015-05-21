import sys
import math

"""
    Write a function to find the longest common prefix string amongst an array of strings.
"""
def longest_common_prefix(a):
    n = len(a)

    if n < 2:
        return a[0] if n == 1 else ""

    prefix = a[0]
    k = len(prefix)
    for i in range(1, n):
        k = min(k, len(a[i]))
        for j in reversed(range(0, k)):
            if prefix[j] != a[i][j]:
                k = j

    return prefix[:k]


#a = [
#    'abaabba',
#    'abba'
#]

#print longest_common_prefix(a)
