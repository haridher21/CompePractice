def heightBalancedBinaryTree(tree): # O(N) T O(H) S
    return False if type(hbbt(tree)) == list else True

def hbbt(tree):
    if not tree:
        return 0
    lh = hbbt(tree.left)
    rh = hbbt(tree.right)
    if type(lh) == list or type(rh) == list:
        return [False]
    if abs(lh - rh) > 1:
        return [False]
    return max(lh, rh) + 1
