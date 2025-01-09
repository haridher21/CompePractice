class Split:
    def __init__(self, goal):
        self.split_sum = 0
        self.subtree_sum = 0
        self.goal = goal


def splitBinaryTree(tree): # O(N) T O(H) S Optimal. But not anywhere as elegant as theirs
    # To make it more elegant, realise why root special case is not needed, and also why we don't really need the subtree sum once its matched
    if not tree:
        return 0
    sum = getSum(tree, 0)
    if sum % 2 == 1: # Can't split if the sum is odd
        return 0
    split = Split(sum / 2)
    # Root case is special, so handling here
    lsplit = checkSum(tree.left, split.goal)
    if lsplit.split_sum:
        return lsplit.split_sum
    rsplit = checkSum(tree.right, split.goal)
    if rsplit.split_sum:
        return rsplit.split_sum

    if (lsplit.subtree_sum + tree.value) == lsplit.goal:
        return lsplit.goal
    if (rsplit.subtree_sum + tree.value) == rsplit.goal:
        return rsplit.goal
    return 0

def getSum(tree, sum):
    if tree:
        l_sum = getSum(tree.left, 0)
        r_sum = getSum(tree.right, 0)
        sum = l_sum + r_sum + tree.value
    return sum

def checkSum(tree, goal):
    split = Split(goal)
    if not tree:
        return split

    lsplit = checkSum(tree.left, goal)
    if lsplit.split_sum:
        return lsplit
    rsplit = checkSum(tree.right, goal)
    if rsplit.split_sum:
        return rsplit

    split.subtree_sum = lsplit.subtree_sum + rsplit.subtree_sum + tree.value
    if split.subtree_sum == split.goal:
        split.split_sum = split.goal
    return split
