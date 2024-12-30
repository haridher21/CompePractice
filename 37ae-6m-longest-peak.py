def longestPeak(array): # O(N)
    r, d, peak = 0, 0, 0 # r is rise, d is descent
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            if d > 0:
                peak = max(peak, r + d + 1)
                r, d = 0, 0
            r += 1
        elif array[i] > array[i + 1]:
            if r > 0:
                d += 1
        elif array[i] == array[i + 1]:
            if d > 0:
                peak = max(peak, r + d + 1)
            r, d = 0, 0
    if d > 0:
        peak = max(peak, r + d + 1)
    return peak
                
