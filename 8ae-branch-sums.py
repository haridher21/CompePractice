def branchSums(root):
    return bsum([], root, 0) if root else []

def bsum(sumlist, root, rsum):
    rsum += root.value
    if root.left == None and root.right == None:
        sumlist.append(rsum)
    if root.left:
        sumlist = bsum(sumlist, root.left, rsum)
    if root.right:
        sumlst = bsum(sumlist, root.right, rsum)
    return sumlist
