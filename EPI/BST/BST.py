class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.next = None
        self.count = 0
        self.locked = False # 10_17

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
        if val == None:
            val = 'N'
        print ' ' * 4 * level + str(val)
        print ' '
        bst_print_help(root.left, level + 1, output)

def bst_node_count(root):
    if not root:
        return 0

    return bst_node_count(root.left) + bst_node_count(root.right) + 1

def generate_complete_bst(node_count):
    if not node_count:
        return None

    depth = 1
    while 2 ** depth - 1 <= node_count:
        depth += 1

    depth -= 1
    count = [0]
    bottom_level_count = [node_count - (2 ** depth - 1)]
    root = generate_complete_bst_help(0, depth, count, bottom_level_count)
    return root

def generate_complete_bst_help(curr_depth, max_depth, count, bottom_level_count):
    if curr_depth == max_depth:
        if bottom_level_count[0] <= 0:
            return None

        bottom_level_count[0] -= 1
        res = Node(count[0])
        count[0] += 1
        return res

    l = generate_complete_bst_help(curr_depth + 1, max_depth, count, bottom_level_count)
    root = Node(count[0])
    count[0] += 1
    r = generate_complete_bst_help(curr_depth + 1, max_depth, count, bottom_level_count)

    root.left, root.right = l, r
    return root
