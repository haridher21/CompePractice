def maxSubsetSumNoAdjacent(array): # O(N) T O(1) Optimal, but could be written better
    # I am making use of last 3, but just last 2 is sufficient without array mod
    n = len(array)
    if n == 0:
        return 0
    maxv = max(array)
    if n < 3:
        return maxv
    if n == 3:
        return max(maxv, array[1], array[0] + array[2])
    array[2] = max(array[2], array[0] + array[2])
    for i in range(3, n):
        array[i] = max(array[i], array[i] + array[i-2], array[i] + array[i-3])
    return max(array[n-1], array[n-2])
