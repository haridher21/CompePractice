def reverseLinkedList(head):
    prev, cur = None, head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
