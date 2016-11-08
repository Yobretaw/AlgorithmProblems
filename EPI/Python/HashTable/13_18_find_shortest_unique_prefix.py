import os
import math
import sys
from collections import defaultdict, Counter


"""
    Write a function that takes as input and string a set of strings, and returns
    the shortest prefix of the string which is not a prefix of any string in
    the set.
"""
# brute force
def find_prefix(s, str_set):
    if not s or not str_set:
        return '' if not s else s

    prefixs = set()
    for ss in str_set:
        for i in range(1, len(ss) + 1):
            prefixs.add(ss[:i])

    for i in range(1, len(s) + 1):
        if s[:i] not in prefixs:
            return s[:i]

    return ''

# a little better
def find_prefix2(s, str_set):
    if not s or not str_set:
        return '' if not s else s

    j = 1
    for curr in str_set:
        i = j
        while i <= len(s) + 1:
            ss = s[:i]
            if curr.startswith(ss):
                i += 1
                continue
            else:
                j = i
                break

        if i > len(s) + 1:
            return ''
        elif j == len(s):
            break

    return s[:j]

# using trie if the string set remains unchanged
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

    def query(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
        return True

    def longest_prefix(self, s):
        if len(self.root) == 0:
            return s

        curr = self.root
        for i, c in enumerate(s):
            if c in curr:
                curr = curr[c]
            else:
                return s[:i+1]
        return ''


class PrefixFinder:
    def __init__(self, str_set):
        self.trie = Trie()
        for s in str_set:
            self.trie.insert(s)

    def find_shortest_prefix(self, s):
        return self.trie.longest_prefix(s)


str_set = set(['dog', 'be', 'cut'])
print find_prefix('cat', str_set)
print find_prefix2('cat', str_set)
print PrefixFinder(str_set).find_shortest_prefix('cat')

print '=' * 100

str_set = set(['dog', 'be', 'cut', 'car'])
print find_prefix('cat', str_set)
print find_prefix2('cat', str_set)
print PrefixFinder(str_set).find_shortest_prefix('cat')

print '=' * 100

str_set = set(['dog', 'be', 'cut', 'car', 'cat'])
print find_prefix('cat', str_set)
print find_prefix2('cat', str_set)
print PrefixFinder(str_set).find_shortest_prefix('cat')
