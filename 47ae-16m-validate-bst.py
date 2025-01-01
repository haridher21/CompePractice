def validateBst(tree, minv = float("-inf"), maxv = float("inf")): # O(N) T O(D) S Avg
    if not tree:
        return True
    if tree.value < minv:
        return False
    if tree.value >= maxv:
        return False
    left_validation, right_validation = True, True
    if tree.left:
        left_validation = validateBst(tree.left, minv, tree.value)
    if tree.right:
        right_validation = validateBst(tree.right, tree.value, maxv)
        
    return left_validation and right_validation 

"""
def validateBst(tree, nodelist=[]): # O(N) T Not clean what my space is, should be more than O(D^2)?
    # HINT : But instead of nodelist, I should pass min and max value
    if not tree:
        return True
    for value, path_type in nodelist:
        if path_type == "left" and tree.value >= value:
            return False
        if path_type == "right" and tree.value < value:
            return False
    left_validation, right_validation = True, True
    if tree.left:
        nodelist.append([tree.value, "left"])
        left_validation = validateBst(tree.left, nodelist)
        nodelist.pop()
    if tree.right:
        nodelist.append([tree.value, "right"])
        right_validation = validateBst(tree.right, nodelist)
        nodelist.pop()
        
    return left_validation and right_validation
"""
