def firstDuplicateValue(array): # O(N) T O(1) S
    # HINT : Think indices

    # O(N) TS
    """
    d = {}
    for i in array:
        if i in d:
            return i
        d[i] = True
    return -1
    """
