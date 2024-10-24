def sortedSquaredArray(array): #O(N) T&S
    m = len(array)
    p, n, z = 0, 0, 0
    for v in array:
        if v < 0:
            n += 1
        elif v > 0:
            p += 1
        else:
            z += 1
    p1, n1 = n + z, n - 1 # p1 and n1 represent the indexes of the smallest positive and 
    # largest negative number respectively. 
    out = [None for i in range(m)]
    for i in range(z):
        out[i] = 0
    while n1 >= 0 and p1 < m:
        ps = array[p1] * array[p1]
        ns = array[n1] * array[n1]
        if ps >= ns:
            out[z] = ns
            n1 -= 1
        else:
            out[z] = ps
            p1 += 1
        z += 1
    while n1 >= 0:
        ns = array[n1] * array[n1]
        out[z] = ns
        n1 -= 1
        z += 1
    while p1 < m:
        ps = array[p1] * array[p1]
        out[z] = ps
        p1 += 1
        z += 1
        
    return out
