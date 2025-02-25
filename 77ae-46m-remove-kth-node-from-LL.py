def removeKthNodeFromEnd(head, k):
    # This 2 moving pointer method also works, but their solution is cooler, even if same complexity
    # Basically, move by k first, then move both pointers, until the forward one reaches the end, at which point the one behind is exactly k behind.
    cur1, cur2, count = head, head, 0
    while cur2:
        count += 1
        cur1 = cur1.next
        cur2 = cur2.next
        if cur2:
            cur2 = cur2.next
    fromStart = (2 * count) - k
    if fromStart < 0:
        return
    elif fromStart == 0:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev, cur = None, head
        while fromStart > 0:
            fromStart -= 1
            prev, cur = cur, cur.next
        prev.next = cur.next
