def twoNumberSum(array, targetSum):
    # While this works, I feel it doesn't include the case if the numbers could actually repeat
    # O(n) solution, but actually should fail
    i, n = 0, len(array)
    while i < n:
        second = targetSum - array[i]
        if array[i] != second and second in array:
            return [second, array[i]]
        i += 1
    return []
