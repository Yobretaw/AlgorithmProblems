class Node():
    def __init__(self, val, left=None, right=None, parent=None, store=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.next = None
        self.count = 0
        self.locked = False # 10_17

        self.store = store
        self.size = 1 + (left.size if left else 0) + (right.size if right else 0)

    def __repr__(self):
        return str(self.val)


def bst_print(root, print_size=False):
    bst_print_help(root, 0, print_size)

def bst_print_help(root, level, print_size):
    if root:
        bst_print_help(root.right, level + 1, print_size)
        val = root.val
        if val == None:
            val = 'N'
        print ' ' * 4 * level + str(val) + (('[%s]' % root.size) if print_size else '')
        print ' '
        bst_print_help(root.left, level + 1, print_size)

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

def bst_to_array(root):
    if not root:
        return []

    return bst_to_array(root.left) + [root] + bst_to_array(root.right)

def build_bst_from_sorted_array(arr):
    n = len(arr)
    return build_bst_from_sorted_array_help(arr, 0, n)

def build_bst_from_sorted_array_help(arr, start, end):
    if start == end:
        return None

    if start == end - 1:
        res = arr[start]
        res.left = res.right = None
        return res

    mid = start + (end - start) / 2
    root = arr[mid]

    root.left = build_bst_from_sorted_array_help(arr, start, mid)
    root.right = build_bst_from_sorted_array_help(arr, mid + 1, end)

    return root

def bst_insert_node(root, val, store=None):
    arr = bst_to_array(root) + [Node(val=val, store=store)]
    arr.sort(key=lambda x: x.val)

    return build_bst_from_sorted_array(arr)

def bst_remove_node(root, val):
    arr = bst_to_array(root)
    arr = filter(lambda x: x.val != val, arr)
    return build_bst_from_sorted_array(arr)


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
    root_val = count[0]
    count[0] += 1
    r = generate_complete_bst_help(curr_depth + 1, max_depth, count, bottom_level_count)

    root = Node(root_val, l, r)
    return root

def find_node(root, val):
    if not root:
        return None

    while root:
        if root.val == val:
            return root

        root = root.left if root.val > val else root.right
    return None

