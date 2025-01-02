# Suboptimal. Hint for optimal : Recursively call both subtree, before constructing the node with the 2 subtree returned


def reconstructBst(preOrderTraversalValues): # NlogN though, suboptimal
    n = len(preOrderTraversalValues)
    if n == 0:
        return
    root = BST(preOrderTraversalValues[0])
    for i in range(1, n):
        new_node = BST(preOrderTraversalValues[i])
        insert(root, new_node)
    return root

def insert(root, new_node):
    cur = root
    while cur:
        prev = cur
        if new_node.value < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    if new_node.value < prev.value:
        prev.left = new_node
    else:
        prev.right = new_node
