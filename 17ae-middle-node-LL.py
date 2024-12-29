def middleNode(linkedList):
    cur, cur2 = linkedList, linkedList
    while cur and cur.next:
        if cur.next.next:
            cur = cur.next.next
            cur2 = cur2.next
        else:
            return cur2.next
    return cur2
