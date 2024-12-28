    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array
