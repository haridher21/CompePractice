def smallestDifference(arrayOne, arrayTwo): #T nlogn + mlogm, S 1
    d = {}
    for val in arrayOne: # n, n
        d[val] = 1
    for val in arrayTwo: # m, m
        if val in d:
            return [val, val]
        d[val] = 0
        
    arrayOne.sort() # nlogn
    arrayTwo.sort() # mlogm
    i, j, n, m, minOne, minTwo, minv = 0, 0, len(arrayOne), len(arrayTwo), 0, 0, float("inf")
    
    while i < n and j < m: # n + m
        oneSmaller = True if arrayOne[i] < arrayTwo[j] else False
        if oneSmaller:
            if abs(arrayOne[i] - arrayTwo[j]) < minv:
                minOne, minTwo, minv = i, j, abs(arrayOne[i] - arrayTwo[j])
            i += 1
        else:
            if abs(arrayOne[i] - arrayTwo[j]) < minv:
                minOne, minTwo, minv = i, j, abs(arrayOne[i] - arrayTwo[j])
            j += 1
    return [arrayOne[minOne], arrayTwo[minTwo]]


""" O(N^2)
def smallestDifference(arrayOne, arrayTwo):
    minv = float("inf")
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if abs(arrayTwo[j] - arrayOne[i]) < minv:
                minv = abs(arrayTwo[j] - arrayOne[i])
                minIdx1, minIdx2 = i, j
    return [arrayOne[minIdx1], arrayTwo[minIdx2]]
"""
