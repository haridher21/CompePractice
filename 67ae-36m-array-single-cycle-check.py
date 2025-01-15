def hasSingleCycle(array): # O(N) T O(1) S
    n , count = len(array), 1
    loc = (array[0]) % n
    while count < n and loc != 0:
        count += 1
        loc = (loc + array[loc]) % n
    return loc == 0 and count == n

"""
def hasSingleCycle(array): # O(N) TS
    n, count, loc = len(array), 0, 0
    visited = [False] * n
    while count < n:
        if visited[loc] == True:
            return False
        visited[loc] = True
        count += 1
        loc = (loc + array[loc]) % n
    return True if loc == 0 else False
"""
