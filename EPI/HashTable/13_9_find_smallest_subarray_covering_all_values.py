import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function which takes an array of strings and a set of strings and
    return the indices of the starting and ending index of a shortest subarray
    of the given array that "covers" the set, i.e., contains all strings in the
    set.

    ====
     
    Same as Leetcode: Minimum Window Substring
"""
def find_smallest_subarray_covering_set(s, t):
    if not t or not s or len(s) < len(t):
        return ""

    m, n = len(s), len(t)
    allchar = Counter(t)
    seen = defaultdict(int)

    start, end = 0, sys.maxint
    count = 0

    i = j = 0
    while j < m:
        while j < m and count < n:
            if s[j] in allchar:
                if seen[s[j]] < allchar[s[j]]:
                    count += 1
                seen[s[j]] += 1
            j += 1

        if count < n:
            break

        while i < j:
            if not s[i] in allchar:
                i += 1
            elif seen[s[i]] > allchar[s[i]]:
                seen[s[i]] -= 1
                i += 1
            else:
                if (j - i) < (end - start):
                    start, end = i, j
                break

        if i < j:
            seen[s[i]] -= 1
            i += 1
            count -= 1

    if end == sys.maxint:
        return ''
    return s[start:end]


"""
    Variant 13.9.2
    
    Given an array A, find a shortest subarray A[i:j] such that each distinct
    value present in A is also present in the subarray.
"""
def subarray_cover(a):
    n = len(a)
    if n < 2:
        return (-1, -1) if not a else (0, 0)
    
    vals = set(a)
    return find_smallest_subarray_covering_set(a, vals)


"""
    Variant 13.9.3

    Given an array A, rearrange the elements so that the shortest subarray
    containing all distinct values in A has maximum possible length
"""
def rearrange(a):
    n = len(a)
    if n < 2:
        return
    
    # probably no need to sort...
    a[:] = ''.join(sorted(a))
    c = Counter(a)

    least_common = c.most_common()[-2:]

    a[:] = list(filter(lambda x: x != least_common[0][0], a))
    a[:] = list(filter(lambda x: x != least_common[1][0], a))

    a[:] = [least_common[0][0]] * least_common[0][1] + a
    a[:] = a + [least_common[1][0]] * least_common[1][1]


"""
    Variant 13.9.4

    Given an array A and a positive integer k, rearrange the elements so that
    no two equal elements are k or less apart.
"""
def rearrange2(s, dist):
    n = len(s)
    if n < 2:
        return s

    s = ''.join(p[0] * p[1] for p in Counter(s).most_common())

    arr = [None] * n
    cur = 0
    for c in s:
        while arr[cur] != None:
            cur += 1
            cur %= n

        prev_char = arr[cur - 1] if cur > 0 else None
        next_char = arr[cur + 1] if cur < n - 1 else None
        if c == prev_char or c == next_char:
            raise Exception('Cannot rearrange')

        arr[cur] = c
        cur += dist
        cur %= n

    return ''.join(arr) 


"""
    Variant 13.9.5

    Given an array A, find a longest subaray A[i:j] such that all elements in
    A[i:j] are distinct.
"""
def find_longest_subarray_without_dupilcates(s):
        n = len(s)
        if n < 2:
            return s

        i = 0
        start, end = 0, -1
        latest_pos = {}
        for j, char in enumerate(s):
            if char in latest_pos:
                i = max(i, latest_pos[char] + 1)

            latest_pos[char] = j

            if (j - i + 1) > (end - start + 1):
                start, end = i, j

        return s[start:end+1]



if __name__ == '__main__':
    #print find_smallest_subarray_covering_set('ADOBECODEBANC','ABC')
    #print find_smallest_subarray_covering_set('aa','a')
    #print find_smallest_subarray_covering_set('aa','ab')

    #A = list('ADOBECODEBANC')
    #rearrange(A)
    #print A

    # tests for rearrange2
    #print rearrange2(list('aaaabbbcc'), 2)
    #print rearrange2(list('geeksforgeeks'), 3)
    #print rearrange2(list('aaaabbbcc'), 3)

    #print find_longest_subarray_without_dupilcates('geeksforgeeks')
