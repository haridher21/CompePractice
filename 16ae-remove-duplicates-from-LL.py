def removeDuplicatesFromLinkedList(linkedList): # O(N) TS
    if not linkedList:
        return
    d = {}
    prev = linkedList
    cur = prev.next
    d[prev.value] = True
    while cur:
        if cur.value in d:
            node_to_delete = cur
            cur = cur.next
            prev.next = cur
            print(f"We're deleting {node_to_delete.value}")
            del(node_to_delete)
        else:
            d[cur.value] = True
            prev, cur = cur, cur.next
    return linkedList
