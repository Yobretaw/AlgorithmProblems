import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

    Calling next() will return the next smallest number in the BST.

    Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.path = []

        next_node = self.root
        while next_node:
            self.path.append(next_node)
            next_node = next_node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.path) != 0

    # @return an integer, the next smallest number
    def next(self):
        res = self.path.pop()
        if res.right:
            succ = res.right
            while succ:
                self.path.append(succ)
                succ = succ.left
        return res.val

root = Node(1, Node(2), Node(3, Node(4, Node(6), Node(7)), Node(5, Node(8), Node(9))))
#root = Node(1, Node(2), Node(3))
#root = Node(1)
it = BSTIterator(root)
while it.hasNext():
    print it.next()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
