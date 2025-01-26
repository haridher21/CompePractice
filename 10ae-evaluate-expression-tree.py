def evaluateExpressionTree(tree):
    return et(tree)

def et(tree):
    if not tree.value < 0:
        return tree.value
    if tree.value == -1:
        return et(tree.left) + et(tree.right)
    elif tree.value == -2:
        return et(tree.left) - et(tree.right)
    elif tree.value == -3:
        return int(et(tree.left) / et(tree.right))
    elif tree.value == -4:
        return et(tree.left) * et(tree.right)

