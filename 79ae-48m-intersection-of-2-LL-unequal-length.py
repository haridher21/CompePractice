def mergingLinkedLists(linkedListOne, linkedListTwo):
    # O(N1+N2) T O(1) S
    cur, count1 = linkedListOne, 0
    while cur:
        count1 += 1
        cur = cur.next
    cur, count2 = linkedListTwo, 0
    while cur:
        count2 += 1
        cur = cur.next
    if count1 < count2:
        smaller, bigger = linkedListOne, linkedListTwo
        diff = count2 - count1
    else:
        smaller, bigger = linkedListTwo, linkedListOne
        diff = count1 - count2

    while diff > 0:
        diff -= 1
        bigger = bigger.next

    while smaller and bigger:
        if smaller.value == bigger.value:
            return smaller # or bigger
        smaller, bigger = smaller.next, bigger.next

    return None # No matches

"""
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # O(N) TS Suboptimal
    d = {}
    matched = None
    cur1, cur2 = linkedListOne, linkedListTwo
    while cur1: # O(N1)
        d[cur1.value] = True
        cur1 = cur1.next
    while cur2: # O(N2)
        if cur2.value in d:
            matched = cur2.value
            break
        cur2 = cur2.next
    if matched:
        return cur2
    return None
 """           
