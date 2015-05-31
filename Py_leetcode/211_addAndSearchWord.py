import sys
import math
import imp
from collections import defaultdict

Trie = imp.load_source('Trie', './208_implementTrie.py').Trie

"""
    Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

    For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
"""
class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val=None):
        self.val = val
        self.children = {}  # char -> node
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        n = len(word)
        curr = self.root
        for i in range(n):
            char = word[i]
            if not char in curr.children:
                for j in range(i, n):
                    curr.children[word[j]] = TrieNode()
                    curr = curr.children[word[j]]
                break
            else:
                curr = curr.children[char]
        curr.val = word
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word, start=0):
        n = len(word)
        curr = self.root

        i = 0
        while i < start:
            curr = curr.children[word[i]]
            i += 1

        for i in range(start, n):
            char = word[i]
            if char != '.' and not char in curr.children:
                return False
            elif char == '.':
                for c in curr.children:
                    s = word[:i] + c + word[i + 1:]
                    if self.search(s, i):
                        return True
                return False
            curr = curr.children[char]
        return curr.val == word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        n = len(prefix)
        curr = self.root
        for i in range(n):
            char = prefix[i]
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return True


class WordDictionary:
    def __init__(self):
        self.t = Trie()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.t.insert(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.t.search(word)
        

# Your WordDictionary object will be instantiated and called as such:
#wordDictionary = WordDictionary()
#wordDictionary.addWord("wordabcd")
#print wordDictionary.search("word...")
