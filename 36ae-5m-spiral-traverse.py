def spiralTraverse(array): # O(N * M) T S or O(n) where n = N * M
   # This is optimal, but could be written simpler
    n, m, i, j = len(array), len(array[0]), 0, 0
    visited, final = [[False for _ in range(m)] for _ in range(n)], []
    v_count, total = 0, m * n
    print(visited)
    
    while v_count < total:
        while j < m and not visited[i][j]: # Right
            final.append(array[i][j])
            visited[i][j] = True
            v_count += 1
            j += 1
        j -= 1
        i += 1
        while i < n and not visited[i][j]: # Down
            final.append(array[i][j])
            visited[i][j] = True
            v_count += 1
            i += 1
        i -= 1
        j -= 1
        while j >= 0 and not visited[i][j]: # Left
            final.append(array[i][j])
            visited[i][j] = True
            v_count += 1
            j -= 1
        j += 1
        i -= 1
        while i >= 0 and not visited[i][j]: # Up
            final.append(array[i][j])
            visited[i][j] = True
            v_count += 1
            i -= 1
        i += 1
        j += 1
    return final
