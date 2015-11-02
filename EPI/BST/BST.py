class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.next = None
        self.count = 0
        self.locked = False # 10_17

        self.store = None

    def __repr__(self):
        return str(self.val)


def bst_print(root):
    bst_print_help(root, 0)

def bst_print_help(root, level):
    if root:
        bst_print_help(root.right, level + 1)
        val = root.val
        if val == None:
            val = 'N'
        print ' ' * 4 * level + str(val)
        print ' '
        bst_print_help(root.left, level + 1)

def bst_node_count(root):
    if not root:
        return 0

    return bst_node_count(root.left) + bst_node_count(root.right) + 1

def bst_get_leftmost(root):
    while root and root.left:
        root = root.left
    return root

def bst_get_rightmost(root):
    while root and root.right:
        root = root.right
    return root

def bst_insert_node(root, val, store=None):
    new_node = Node(val=val, store=store)

    if not root:
        return new_node

    parent = None
    while root:
        parent = root
        if root.val > val:
            root = root.left
        else:
            root = root.right

    if root.val < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    return root

def bst_remove_node(root, val):
    if not root:
        return None

    res = parent = Node(root.val + 1, root, None)
    while root:
        if root.val == val:
            right_tree = root.right
            if parent.val > root.val:
                parent.left = root.left
            else:
                parent.right = root.left
            root = root.left
            while root.right:
                root = root.right
            root.right = right_tree
        parent = root
    return res.left


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

def find_node(root, val):
    if not root:
        return None

    while root:
        if root.val == val:
            return root

        root = root.left if root.val > val else root.right
    return None

