def rearrangeLinkedList(head, k):
    # I've done some manipulation, and couldn't quite figure out the moving the matching nodes
    # But if we're allowed to just create those ones, I've got it.

    # But the idea is on the right
    
    # Let's identify the node with the value k first if present
    # We'll actually remove all of them, but keep the count of them and add back later
    print(k)
    printnodes("Original", head)
    prev, cur = None, head
    kfound = 0
    while cur:
        if cur.value == k:
            # Build the segment of nodes for k
            kfound += 1
            
            if prev:
                prev.next = cur.next if cur.next else None
            else: # Very first entry
                if head.next == None: # Only 1 entry in LL
                    return head
                # If not, we replace the head with the values of the 2nd node, and then skip the 2nd
                head.value = head.next.value
                node = head.next
                head.next = head.next.next
                del(node)
                cur = head
                continue
                
            cur = cur.next
            continue
        prev, cur = cur, cur.next

    printnodes("k-removed", head)
    #printnodes("k", khead)

    # Now that this is working as expected, let's start shifting the nodes to the left and right
    cur, lprev, rprev = head, None, None
    lstart, rstart = None, None
    # We split the LL into left and right segments
    while cur:
        if cur.value < k:
            if lprev: # If previous exists, it should now point to this new current node
                lprev.next = cur
            else:
                lstart = cur
            lprev, cur = cur, cur.next # Move the previous and current forward
        else: # Same for right/greater
            if rprev:
                rprev.next = cur
            else:
                rstart = cur
            rprev, cur = cur, cur.next

    if lprev:
        lprev.next = None
    if rprev:
        rprev.next = None
        
    printnodes("lesser", lstart)
    printnodes("greater", rstart)

    # Joining back, by also adding the k nodes
    if lstart:
        while kfound > 0:
            kfound -= 1
            node = LinkedList(k)
            lprev.next = node
            lprev = node
        lprev.next = rstart
        printnodes("Joined", lstart)
        return lstart
    else:
        if kfound:
            kstart = LinkedList(k)
            kfound -= 1
            kprev = kstart
            while kfound > 0:
                kfound -= 1
                node = LinkedList(k)
                kprev.next = node
            kprev.next = rstart
            return kstart
        else:
            return rstart
            



def printnodes(st, head):
    cur = head
    print(st, end = " : ")
    while cur:
        print(cur.value, end = ",")
        cur = cur.next
    print()
