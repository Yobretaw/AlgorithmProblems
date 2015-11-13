import imp

ListNode = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list


"""
    Given a singly linked list, determine if it is a palindrome.
"""
def palindrome_linked_list(l):
    if not l or not l.next:
        return True

    # find the head of the second half of the list
    prev = ListNode('', l)
    curr = prev.next
    fast = l
    while fast and fast.next:
        fast = fast.next.next
        curr = curr.next
        prev = prev.next

    prev.next = None

    # now curr is the head of the second half, flip the second half
    head = None
    while curr:
        tmp = curr.next
        curr.next = head
        head = curr
        curr = tmp

    # compare two lists
    first, second = l, head
    while first and second:
        if first.val != second.val:
            return False
        first, second = first.next, second.next

    return True


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
    l = ListNode(1, ListNode(0, ListNode(1)))
    print palindrome_linked_list(l)
