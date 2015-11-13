import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
"""
def lowest_common_ancestor(root, a, b):
    if not root:
        return None

    if a is root or b is root:
        return root

    l = lowest_common_ancestor(root.left, a, b)
    r = lowest_common_ancestor(root.right, a, b)

    if l and r:
        return root
    else:
        return l or r


if __name__ == '__main__':
    pass
