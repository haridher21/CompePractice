def shiftLinkedList(head, k):
    count, cur = 0, head
    while cur:
        count += 1
        cur = cur.next
    k = k % count
    cur, prev, diff = head, None, count - k
    if diff <= 0 or k == 0:
        return head

    while diff > 0:
        diff -= 1
        prev = cur
        cur = cur.next
    newHead = cur
    prev.next = None

    while cur.next:
        cur = cur.next
    cur.next = head
    return newHead
