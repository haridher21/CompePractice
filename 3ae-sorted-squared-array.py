def sortedSquaredArray(array):
    p , z, n, pos, neg, length = 0, 0, 0, 0, 0, len(array)
    for i in array: # Get count of pos, neg numbers and zeroes
        if i < 0:
            n += 1
        elif i == 0:
            z += 1
        else:
            p += 1
    narray = [0 for _ in range(z)] # Add the zeroes in first
    neg = n - 1 # Start at first negative number
    pos = n + z # Start at first positive number
    while neg >= 0 and pos < length:
        n2 = array[neg] * array[neg]
        p2 = array[pos] * array[pos]
        if n2 < p2:
            neg -= 1
            narray.append(n2)
        elif n2 > p2:
            pos += 1
            narray.append(p2)
        else:
            neg -= 1
            pos += 1
            narray.append(n2)
            narray.append(p2)
    while neg >= 0: # Handling left over negative numbers
        narray.append(array[neg] * array[neg])
        neg -= 1
    while pos < length: # Handling left over positive numbers
        narray.append(array[pos] * array[pos])
        pos += 1
    return narray
