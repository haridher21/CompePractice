def generateDocument(characters, document):
    lc = len(characters)
    if lc < len(document):
        return False
    d = {}
    setc, setd = set(characters), set(document)
    for c in setc:
        d[c] = 0
    for c in setd:
        if c not in d:
            return False
    for c in characters:
        d[c] += 1
    for c in document:
        d[c] -= 1
    for key in d:
        if d[key] < 0:
            return False
    return True
