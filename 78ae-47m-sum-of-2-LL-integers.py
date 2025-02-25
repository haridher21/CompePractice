def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    cur1, cur2 = linkedListOne, linkedListTwo
    if cur1 == None:
        return cur2
    if cur2 == None:
        return cur1

    prev, cur, newHead = None, None, None
    carry = 0
    while cur1 and cur2:
        sum = cur1.value + cur2.value + carry
        digit, carry = sum % 10, sum // 10
        prev, cur = cur, LinkedList(digit)
        cur1, cur2 = cur1.next, cur2.next
        if prev == None:
            newHead = cur
            continue
        prev.next = cur
        

    bigger = cur1 if cur1 else cur2
    while bigger:
        sum = bigger.value + carry
        digit, carry = sum % 10, sum // 10
        bigger = bigger.next
        prev, cur = cur, LinkedList(digit)
        prev.next = cur

    if carry:
        prev, cur = cur, LinkedList(carry)
        prev.next = cur

    return newHead
