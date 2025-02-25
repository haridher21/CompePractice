def removeDuplicatesFromSortedLinkedList(linkedList):
    cur = linkedList
    while cur.next:
        next = cur.next
        if cur.value == next.value:
            cur.next = next.next
        else:
            cur = next
    return linkedList
