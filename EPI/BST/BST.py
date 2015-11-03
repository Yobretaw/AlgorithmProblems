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

def bst_to_array(root):
    if not root:
        return []

    print root
    return bst_to_array(root.left) + [root] + bst_to_array(root.right)

def build_bst_from_sorted_array(arr):
    n = len(arr)
    return build_bst_from_sorted_array_help(arr, 0, n)

def build_bst_from_sorted_array_help(arr, start, end):
    if start == end:
        return None

    if start == end - 1:
        return arr[start]

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

#def bst_insert_node(root, val, store=None):
#    new_node = Node(val=val, store=store)

#    if not root:
#        return new_node

#    root_copy = root
#    parent = None
#    while root:
#        parent = root
#        if root.val > val:
#            root = root.left
#        else:
#            root = root.right

#    if val < parent.val:
#        parent.left = new_node
#    else:
#        parent.right = new_node

#    return root_copy

#def bst_remove_node(root, val):
#    if not root:
#        return None

#    if root.val == val:
#        if not root.left or not root.right:
#            return root.left if root.left else root.right
#        else:
#            new_root = root.left
#            tmp = new_root
#            while new_root.right:
#                new_root = new_root.right
#            new_root.right = root.right
#            return new_root
#    else:
#        while root:
#            if root.val == val:
#                if root.val < parent.val:
#                    l, r = root.left, root.right
#                    parent.left = l
#                    while l.right:
#                        l = l.right
#                    l.right = r
#                    return
#                else:
#                    l, r = root.left, root.right
#                    parent.right = l
#                    while l.right:
#                        l = l.right
#                    l.right = r
#                    return
#                else:
#                    if root.val < val:
#                        root = root.left
#                    else:
#                        root = root.right
#            parent = root
#    return root


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

