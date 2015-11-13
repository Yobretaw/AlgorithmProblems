import imp

ListNode = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list


"""
    Write a function to delete a node (except the tail) in a singly linked
    list, given only access to that node.

    Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third
    node with value 3, the linked list should become 1 -> 2 -> 4 after
    calling your function.
"""
def delete_node(node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
