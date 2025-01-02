def findKthLargestValueInBst(tree, k): # O(H+K) T, O(H) S # Optimal, just that their solution uses a class to make things more elegant
    found, count = inorder(tree, 0, k)
    if found:
        return found[0]
    return None


def inorder(tree, count, k, found = None):
    if tree:
        found, count = inorder(tree.right, count, k)
        if found:
            return found, count
        count += 1
        if count == k:
            return [[tree.value], count]
        found, count = inorder(tree.left, count, k)
        if found:
            return found, count
    return None, count


"""
def findKthLargestValueInBst(tree, k): #O(N) TS
    array = inorder(tree, [])
    return array[len(array) - k]

def inorder(tree, array):
    if tree:
        array = inorder(tree.left, array)
        array.append(tree.value)
        array = inorder(tree.right, array)
    return array
"""
