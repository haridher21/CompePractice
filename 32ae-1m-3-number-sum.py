def threeNumberSum(array, targetSum): # T n^2, S supposedly n cause we can store n entries potentially
    array.sort() # nlogn
    triplets = []
    for i in range(len(array) - 2): # n
        j, k = i + 1, len(array) - 1
        target = targetSum - array[i]
        while j < k: # n
            sum = array[j] + array[k]
            if sum == target:
                triplets.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif sum < target:
                j += 1
            elif sum > target:
                k -= 1
    return triplets
