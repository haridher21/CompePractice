    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        node = BST(value)
        while True:
            if value < root.value:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    break
        return self

    def contains(self, value):
        # Write your code here
        root = self
        while root:
            if root.value == value:
                return True
            elif value < root.value:
                root = root.left
            else:
                root = root.right
        return False
        pass






    def remove(self, value): # My not so smart implementation, but it should work, and output shows that, but fails the remove testcase
        
        print("Trying to remove:", value)
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        if root.value == value: # Root node itself
            parent = None
        while root:
            if root.value == value:
                replacement = root.findLeftMostinRightSubTree()
                break
            elif value < root.value:
                parent = root
                root = root.left
            else:
                parent = root
        
