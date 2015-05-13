import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

    For example,
    Given n = 3, your program should return all 5 unique BST's shown below.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
"""
def generateTrees(n):
    arr = [i + 1 for i in range(0, n)]
    return generateTrees_help(arr)

def generateTrees_help(arr):
    if not arr:
        return [None]
    if len(arr) == 1:
        return [Node(arr[0])]

    res = []
    for i in range(0, len(arr)):
        left_arr = generateTrees_help(arr[:i])
        right_arr = generateTrees_help(arr[i + 1:])
        for m in range(0, len(left_arr)):
            for n in range(0, len(right_arr)):
                root = Node(arr[i])
                root.left = left_arr[m]
                root.right = right_arr[n]
                res.append(root)
    return res

def generateTreesDP(n):
    if n == 0:
        return [None]
    tree_list = [[[None]] * (n + 2) for i in range(n + 2)]
    for i in range(1, n + 1):
        tree_list[i][i] = [Node(i)]
        for j in reversed(range(1, i)):
            tree_list[j][i] = []
            for k in range(j, i + 1):
                for left in tree_list[j][k - 1]:
                    for right in tree_list[k + 1][i]:
                        root = Node(k)
                        (root.left, root.right) = (left, right)
                        tree_list[j][i].append(root)
    return tree_list[1][n]

#n = 5
#for root in generateTreesDP(n):
#    bst_print(root)
#    print '-' * 100
