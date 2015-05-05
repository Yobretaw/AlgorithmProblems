class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.count = 0

    def __repr__(self):
        return str(self.val)


def bst_generate_tree(n):
    arr = []
    for i in range(0, n):
        arr.append(i)

    pass

def bst_generate_tree_help():
    pass

def bst_print(root):
    output = []
    bst_print_help(root, 0, output)
        

def bst_print_help(root, level, output):
    if root:
        bst_print_help(root.right, level + 1, output)
        val = root.val
        if not val:
            val = 'N'
        print ' ' * 4 * level + str(val)
        print ' '
        bst_print_help(root.left, level + 1, output)
