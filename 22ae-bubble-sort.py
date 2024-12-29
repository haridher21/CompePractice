def bubbleSort(array):
    for i in range(len(array)):
        sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if sorted:
            break
    return array
