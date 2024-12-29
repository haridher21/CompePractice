def firstNonRepeatingCharacter(string):
    d = {}
    for c in string:
        d[c] = 1 if c not in d else d[c] + 1
    for i in range(len(string)):
        if d[string[i]] == 1:
            return i
    return -1
