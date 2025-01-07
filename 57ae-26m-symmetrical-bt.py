# Can be written significantly shorter
def symmetricalTree(tree): # O(N) T O(H) S (space is just stack height) Optimal
    return st(tree, tree)

def st(tree1, tree2):
    c1, c2 = True, True
    if tree1.left:
        if not(tree2.right and tree1.left.value == tree2.right.value):
            return False
        c1 = st(tree1.left, tree2.right)
    elif tree2.right:
        return False
    if tree2.left:
        if not(tree1.right and tree2.left.value == tree1.right.value):
            return False
        c2 = st(tree1.right, tree2.left)
    elif tree1.right:
        return False
    
    if c1 and c2:
        return True
    return False
