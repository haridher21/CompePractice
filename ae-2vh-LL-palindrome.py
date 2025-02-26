def linkedListPalindrome(head): # O(N) T O(1) S
    count, cur = 0, head
    # Get count of nodes
    while cur: # O(N)
        count += 1
        cur = cur.next
    # Check if even or odd palindrome
    if count % 2 == 1:
        half = count // 2 + 1
    else:
        half = count // 2
        
    # Get beyond halfway # O(N)
    lcur, rcur, rprev = head, head, None
    for i in range(half):
        rprev, rcur = rcur, rcur.next

    # Reverse the 2nd half O(N)
    while rcur:
        next = rcur.next
        rcur.next = rprev
        rprev = rcur
        rcur = next

    # Compare the 2 halves O(N)
    for i in range(half):
        if lcur.value != rprev.value:
            return False
        lcur, rprev = lcur.next, rprev.next
    return True
