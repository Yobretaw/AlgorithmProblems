import sys
import math
from heapq import *


"""
    Given:
        A set of symbols and their weights (usually proportional to probabilities).

    Goal:
        Find a prefix-free binary code (a set of codewords) with minimum expected
        codeword length 

    -----

    The simplest construction algorithm of Huffman encoding uses a priority queue
    where the node with lowest probability is given highest priority:

        1. Create a leaf node for each symbol and add it to the priority queue.

        2. While there is more than one node in the queue:

            1. Remove the two nodes of highest priority (lowest probability) from
            the queue

            2. Create a new internal node with these two nodes as children and
            with probability equal to the sum of the two nodes' probabilities.

            3. Add the new node to the queue.

        3. The remaining node is the root node and the tree is complete.

    Since efficient priority queue data structures require O(logn) time per
    insertion, and a tree with n leaves has 2n - 1 nodes, this algorithm operates
    in O(nlogn) time, where n is the number of symbols.

    -----


    Proof of Optimality for Huffman Coding:

        See: http://algoviz.org/OpenDSA/Books/Everything/html/HuffProof.html
"""
class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

        self.left = self.right = None

    def __le__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

class Symbol:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

def build_tree(symbols):
    if not symbols:
        return None
    
    symbols = [Node(s.char, s.freq) for s in symbols]
    heapify(symbols)

    while len(symbols) > 1:
        first, second = heappop(symbols), heappop(symbols)

        node = Node(None, first.freq + second.freq)
        node.left = first
        node.right = second
        
        heappush(symbols, node)

    return symbols[0]

def print_encoding_tree(root, prev=''):
    if not root:
        return

    if not root.left and not root.right:
        print '{0: <10}'.format(prev) + ': '+ root.val
        return

    print_encoding_tree(root.left, prev + '0')
    print_encoding_tree(root.right, prev + '1')

if __name__ == '__main__':
    symbols = [
        Symbol('E', 12.02), Symbol('T', 9.10),
        Symbol('A', 8.12), Symbol('O', 7.68),
        Symbol('I', 7.31), Symbol('N', 6.95),
        Symbol('S', 6.28), Symbol('R', 6.02),
        Symbol('H', 5.92), Symbol('D', 4.32),
        Symbol('L', 3.98), Symbol('U', 2.88),
        Symbol('C', 2.71), Symbol('M', 2.61),
        Symbol('F', 2.30), Symbol('Y', 2.11),
        Symbol('W', 2.09), Symbol('G', 2.03),
        Symbol('P', 1.82), Symbol('B', 1.49),
        Symbol('V', 1.11), Symbol('K', 0.69),
        Symbol('X', 0.17), Symbol('Q', 0.11),
        Symbol('J', 0.10), Symbol('Z', 0.07)
    ]

    t = build_tree(symbols)
    print_encoding_tree(t)
