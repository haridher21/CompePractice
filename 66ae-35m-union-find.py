# They've done some extra stuff, but I think that isn't necessary to have, hence mine should be more optimal I believe
class UnionFind:
    def __init__(self):
        self.set = {}

    def createSet(self, value): # O(1)
        self.set[value] = value

    def find(self, value): # O(1)
        if value in self.set:
            return self.set[value]
        return None

    def union(self, valueOne, valueTwo): #O (N) T
        if valueOne not in self.set or valueTwo not in self.set:
            return
        if self.set[valueOne] != self.set[valueTwo]:
            setOneValue, setTwoValue = self.set[valueOne], self.set[valueTwo]
            for val in self.set:
                if self.set[val] == setTwoValue:
                    self.set[val] = setOneValue
