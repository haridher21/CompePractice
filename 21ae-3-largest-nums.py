def findThreeLargestNumbers(array):
    a, b, c = float("-inf"), float("-inf"), float("-inf")

    for i in range(len(array)):
        cur = array[i]
        if cur > c:
            a, b, c = b, c, cur
        elif cur > b:
            a, b = b, cur
        elif cur > a:
            a = cur
    return [a, b, c]
