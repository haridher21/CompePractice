def kadanesAlgorithm(array): # O(N) T O(1) S
    n = len(array)
    if n == 0:
        return None
    maxv, runningSum = array[0], array[0]
    for i in range(1, n):
        if runningSum + array[i] < array[i]:
            runningSum = array[i]
        else:
            runningSum += array[i]
        maxv = max(maxv, runningSum)
    return maxv
    

