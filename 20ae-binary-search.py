def binarySearch(array, target):
    front, end = 0, len(array) - 1
    while front <= end:
        mid = (front + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            front = mid + 1
        else:
            end = mid - 1
    return -1
