class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Optimal O(H1 + H2) T O(1) S
    h1 = getHeight(descendantOne, topAncestor)
    h2 = getHeight(descendantTwo, topAncestor)
    if h1 > h2:
        more_deep, less_deep = descendantOne, descendantTwo
    else:
        more_deep, less_deep = descendantTwo, descendantOne
    diff = abs(h1 - h2) 
    while diff:
        more_deep = more_deep.ancestor
        diff -= 1
    # Both should be at equal depth now
    while more_deep.name != less_deep.name:
        more_deep, less_deep = more_deep.ancestor, less_deep.ancestor
    return more_deep

def getHeight(d, t):
    c = 0
    while d.name != t.name:
        c += 1
        d = d.ancestor
    return c

"""
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Suboptimal O(H1 + H2) TS
    p1, p2 = descendantOne, descendantTwo
    d = {}
    while p1 != p2:
        if p2.name != topAncestor.name and p2.name in d:
            return p2
        if p1.name != topAncestor.name and p1.name in d:
            return p1
        d[p1.name], d[p2.name] = True, True
        p1 = p1.ancestor if p1.ancestor else p1
        p2 = p2.ancestor if p2.ancestor else p2
    return p1
"""
