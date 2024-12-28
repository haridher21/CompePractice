    def depthFirstSearch(self, array):
        nodelist = [self]
        while nodelist:
            node = nodelist.pop(0)
            array.append(node.name)
            children = node.children
            children.extend(nodelist)
            nodelist = children
        return array
