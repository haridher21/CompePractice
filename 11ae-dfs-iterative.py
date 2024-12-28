    def depthFirstSearch(self, array):
        # Write your code here.
        nodelist = [self]
        while nodelist:
            node = nodelist.pop(0)
            array.append(node.name)
            children = node.children
            children.extend(nodelist)
            nodelist = children
        return array
