def moveElementToEnd(array, toMove): # T: O(n) | S: O(1)
    tmc = 0
    for i in range(len(array)):
        if array[i] == toMove:
            tmc += 1
        else:
            array[i], array[i - tmc] = array[i - tmc], array[i]
    return array
