def mergeBinaryTrees(tree1, tree2):
    return merge(tree1, tree2)

def merge(tree1, tree2): # O(N) T O(H) S . Optimal, but their solution is more elegant to read
    if tree1:
        if tree2:
            tree2.value += tree1.value
            tree2.left = merge(tree1.left, tree2.left)
            tree2.right = merge(tree1.right, tree2.right)
        else:
            tree2 = tree1
    return tree2
