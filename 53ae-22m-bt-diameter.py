def binaryTreeDiameter(tree): # O(N) T O(D) S
    return diameter(tree)["diameter"] - 1 # -1 cause its edges = nodes - 1

def diameter(tree):
    if not tree:
        return {"branch_length": 0, "diameter": 0}
    left = diameter(tree.left)
    right = diameter(tree.right)
    longer_branch = max(left["branch_length"], right["branch_length"]) + 1
    branch_sum_length = left["branch_length"] + right["branch_length"] + 1
    current_max_diameter = max(left["diameter"], right["diameter"], branch_sum_length)
    d = {"branch_length": longer_branch, "diameter": current_max_diameter}
    print("Returning d for node with value:", tree.value, d)
    return d
