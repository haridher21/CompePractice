def findLoop(head):
    # O(N) T
    cur1, cur2, loopMatch = head, head, False
    while True:
        if cur1 == cur2:
            if loopMatch:
                break
            loopMatch = True
        cur1, cur2 = cur1.next, cur2.next.next
    # At this point, they've met. Start cur2 from the head again
    cur2 = head
    while cur1 != cur2:
        cur1, cur2 = cur1.next, cur2.next
    return cur1
