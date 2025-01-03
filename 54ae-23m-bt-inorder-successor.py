def findSuccessor(tree, node): # O (H) T O(1) S
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        while True:
            parent = node.parent
            if not parent or parent.left == node:
                return parent
            else:
                node = parent
