def removeIslands(matrix): # O(NM) TS
    if not(len(matrix) and len(matrix[0])):
        return matrix
    r, c = len(matrix), len(matrix[0])
    indexes = getIndexes(r, c, matrix) # O(N + M), and any nodes with 0 aren't added
    visited = [[False for _ in range(c)] for _ in range(r)] # O(NM)
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i, j in indexes: # Check all these edge nodes 
        # O(NM) worst, as if all nodes are visited, then nothing else to check, and we don't add any nodes with 0
        if visited[i][j]: # Ignore if already visited
            continue
        connected = [[i, j]]
        while connected: # DFS Iterative from initial node along the chain of 1s
            a, b = connected.pop(0)
            if visited[a][b]:
                continue
            visited[a][b] = True
            for dr, dc in directions: # 4 directions from an index
                ur, uc = a - dr, b - dc
                if ur > 0 and ur < r and uc > 0 and uc < c: # Index has to be in range
                    if visited[ur][uc] or not matrix[ur][uc]: # Visited or 0, then skip
                        continue
                    connected.append([ur, uc])
                    # If not visited, and a 1, append as a connected 1 that originated from an edge
    for i in range(1, r - 1): # O(NM)
        for j in range(1, c - 1):
            # Traversing nodes except for edges
            if visited[i][j]: # If visited before, it means its a 1
                continue
            matrix[i][j] = 0 # Can set everything else to 0
    return matrix



def getIndexes(r, c, mat):
    l = []
    for i in range(c):
        if mat[0][i]:
            l.append([0, i])
        if mat[r - 1][i]:
            l.append([r - 1, i])
    for i in range(1, r - 1):
        if mat[i][0]:
            l.append([i, 0])
        if mat[i][c - 1]:
            l.append([i, c - 1])
    return l

def printM(mat):
    r, c = len(mat), len(mat[0])
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = " ")
        print()
