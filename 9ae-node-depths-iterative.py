def nodeDepths(root):
    nodelist, sum = [[root, 0]], 0
    while nodelist:
        node, depth = nodelist.pop(0)
        sum += depth
        if node.left:
            nodelist.append([node.left, depth + 1])
        if node.right:
            nodelist.append([node.right, depth + 1])
    return sum
