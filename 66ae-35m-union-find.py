# They've done some extra stuff, but it isn't necessary to clear their testcases, hence more optimal
# BUT, frankly speaking, in longer testcases, their union is more optimal, since its switches the values of the lower set to join the bigger. Mine is basically whomever is called first, hence suboptimal
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
