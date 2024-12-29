def productSum(array, depth = 0, sum = 0):
    if type(array) == int:
        return array
    else:
        for element in array:
            sum += productSum(element, depth + 1)
        return sum * (depth + 1)
