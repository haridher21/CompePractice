def twoNumberSum(array, targetSum):
    array.sort()
    i, j = 0, len(array)-1
    while i < j:
        if array[i] + array[j] == targetSum:
            return [array[i], array[j]]
        if array[i] + array[j] < targetSum:
            i += 1
        elif array[i] + array[j] > targetSum:
            j -= 1
    return []