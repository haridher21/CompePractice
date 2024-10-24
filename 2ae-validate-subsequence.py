def isValidSubsequence(array, sequence):
    i, j, n, m  = 0, 0, len(array), len(sequence)
    while j < m and i < n:
        if array[i] == sequence[j]:
            i += 1
            j += 1 # Matched
            if j == m:
                return True
        else:
            i += 1
    return False
