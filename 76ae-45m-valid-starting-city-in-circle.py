def validStartingCity(distances, fuel, mpg): # O(N) T O(1) S
    # Different from all proposed solutions, makes me wonder if mine could fail
    # My reasoning essentially was, from a given starting point, if I essentially hit any negatives,
    # means we cannot start from wherever we started, and must look ahead. And resetting to 0, means we
    # starting from there, so it should be fine
    running_sum, start_index = 0, 0
    for i in range(len(fuel)):
        running_sum += (fuel[i] * mpg - distances[i])
        if running_sum < 0:
            running_sum = 0
            start_index = i + 1 
    return start_index



