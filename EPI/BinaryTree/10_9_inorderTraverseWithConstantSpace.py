import sys
import math
import imp
from collections import defaultdict

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print
"""
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    For example,
    [1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].
"""
def inorder_traverse(root):
    if not root:
        return

    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if pred.right:
                pred.right = None
                print curr.val
                curr = curr.right
            else:
                pred.right = curr
                curr = curr.left
        else:
            print curr.val
            curr = curr.right


#root = Node(314, Node(6, Node(271, Node(28), Node(0)), Node(561, None, Node(3, Node(17)))), Node(6, Node(2, None, Node(1, Node(401, None, Node(641)))), Node(271, None, Node(28))))
#bst_print(root)
#inorder_traverse(root)
