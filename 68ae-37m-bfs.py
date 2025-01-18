    def breadthFirstSearch(self, array):
        # Iterative O(N) TS
        nodelist = [self]
        while nodelist:
            node = nodelist.pop(0)
            nodelist.extend(node.children)
            array.append(node.name)
        return array
