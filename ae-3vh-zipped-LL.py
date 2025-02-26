def zipLinkedList(linkedList): # O(N) T O(1) S
    cur, count = linkedList, 0
    while cur:
        count += 1
        cur = cur.next

    half = count // 2 + 1 if count % 2 == 1 else count // 2
    if count < 3: # Base case
        return linkedList
    prev, cur = None, linkedList
    for i in range(half):
        prev, cur = cur, cur.next

    # Let's reverse the 2nd half
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    fcur, scur = linkedList, prev
    for i in range(half + 1):
        fnext, snext = fcur.next, scur.next
        fcur.next = scur
        scur.next = fnext
        fcur, scur = fnext, snext
    if count % 2 == 1:
        scur.next = None
    else:
        fcur.next = None

    return linkedList
