def validStartingCity(distances, fuel, mpg): # O(N) T O(1) S
    running_sum, start_index = 0, 0
    for i in range(len(fuel)):
        running_sum += (fuel[i] * mpg - distances[i])
        if running_sum < 0:
            running_sum = 0
            start_index = i + 1 
    return start_index
