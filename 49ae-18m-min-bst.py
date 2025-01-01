# Given a sorted array, most optimal is O(N) TS, which I did not get. This is my suboptimal solution, which could have been cleaner

# Note the logn part comes from using the insert method.

def minHeightBst(array): # O(nlogn), O(n)
    # Their this solution is better though, since it uses a single mid checker
    # rather than one for left and right
    n = len(array)
    if n == 0:
        return None
    mid = n // 2
    root = BST(array[mid])
    minBst(root, array, 0, mid - 1, mid + 1, n - 1)
    return root

def minBst(root, array, leftStart, leftEnd, rightStart, rightEnd):
    if leftStart <= leftEnd and leftStart >= 0:
        mid = (leftStart + leftEnd) // 2
        root.insert(array[mid])
        minBst(root, array, leftStart, mid - 1, mid + 1, leftEnd)
    if rightStart <= rightEnd and rightEnd < len(array):
        mid = (rightStart + rightEnd) // 2
        root.insert(array[mid])
        minBst(root, array, rightStart, mid - 1, mid + 1, rightEnd)



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
