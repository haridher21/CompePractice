def findClosestValueInBst(tree, target):
    nodelist, min = [tree], tree.value
    while nodelist:
        cur = nodelist.pop(0)
        if cur.value == target:
            return target
        if target < cur.value:
            if cur.left:
                if abs(cur.left.value - target) < abs(min - target):
                    min = cur.left.value
                nodelist.append(cur.left)
        else:
            if cur.right:
                if abs(cur.right.value - target) < abs(min - target):
                    min = cur.right.value
                nodelist.append(cur.right)
    return min
