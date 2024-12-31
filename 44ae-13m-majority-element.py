def majorityElement(array): # O(N) T O(1) S
    # Do read Hint 1, since you probably would forget that
    # HINT for real solution : Counter inc decrease

    
    """
    # O(N^2) T O(1) S
    max_freq, max_element = 0, None
    for i in array:
        freq = 0
        for j in array:
            if i == j:
                freq += 1
        if freq > max_freq:
            max_freq = freq
            max_element = i
    if max_freq > (len(array) // 2):
        return max_element
    print("Shouldn't reach here")
    return max_element
    """
