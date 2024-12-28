def nodeDepths(root):
    return bfs(root, 0)

def bfs(root, depth):
    if not root:
        return 0
    return depth + bfs(root.left, depth + 1) + bfs(root.right, depth + 1)
