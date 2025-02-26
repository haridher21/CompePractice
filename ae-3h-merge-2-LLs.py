def mergeLinkedLists(headOne, headTwo):
    # O(N1 + N2) T O(1) S Optimal, but can still slightly be improved
    cur1, cur2, prev, head = headOne, headTwo, None, None
    if cur1.value < cur2.value:
        head, prev, cur1 = cur1, cur1, cur1.next
    else:
        head, prev, cur2 = cur2, cur2, cur2.next

    while cur1 and cur2:
        if cur1.value < cur2.value:
            prev.next = cur1
            prev, cur1 = cur1, cur1.next
        else:
            prev.next = cur2
            prev, cur2 = cur2, cur2.next

    if cur1:
        prev.next = cur1
    if cur2:
        prev.next = cur2
        
    return head
