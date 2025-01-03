def invertBinaryTree(tree): # O(N) T O(D) S
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
