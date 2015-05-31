import sys
import math
from collections import defaultdict

"""
    Implement a trie with insert, search, and startsWith methods.

    Note:
    You may assume that all inputs are consist of lowercase letters a-z.
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
    def search(self, word):
        n = len(word)
        curr = self.root
        for i in range(n):
            char = word[i]
            if not char in curr.children:
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


# Your Trie object will be instantiated and called as such:
#trie = Trie()
#trie.insert("ab")
#print trie.search("abc")
#print trie.search("ab")
#print trie.startsWith("abc")
#print trie.startsWith("ab")
#trie.insert("ab")
#print trie.search("abc")
#print trie.startsWith("abc")
#trie.insert("abc")
#print trie.search("abc")
#print trie.startsWith("abc")

#False
#True
#False
#True
#False
#False
#True
#True
