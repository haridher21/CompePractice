def isMonotonic(array): # O(N)
    lesser, greater = False, False
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            continue
        elif array[i] > array[i + 1]:
            if lesser:
                return False
            greater = True
        elif array[i] < array[i + 1]:
            if greater:
                return False
            lesser = True
    return True
