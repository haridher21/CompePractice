def findClosestValueInBst(tree, target): # Done recursively, do iterative
    return findClosestValue(tree, target, tree.value)

def findClosestValue(tree, target, min):
    if tree.value == target:
        return target
    if target < tree.value:
        if tree.left:
            if abs(tree.left.value - target) < abs(min - target):
                min = tree.left.value
            return findClosestValue(tree.left, target, min)
    else:
        if tree.right:
            if abs(tree.right.value - target) < abs(min - target):
                min = tree.right.value
            return findClosestValue(tree.right, target, min)
    return min
