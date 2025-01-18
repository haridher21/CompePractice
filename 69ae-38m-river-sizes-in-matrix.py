def riverSizes(matrix): # O(WH) TS But recursive, can be iterative tooo
    if not (len(matrix) > 0 and len(matrix[0]) > 0):
        return []
    nr, nc = len(matrix), len(matrix[0])
    visited = [[False] * nc for _ in range(nr)]
    results = []
    i, j = 0, 0
    while i < nr:
        j = 0
        while j < nc:
            if matrix[i][j] == 0:
                visited[i][j] = True
            if visited[i][j]:
                j += 1
                continue
            pos = [i, j, nr, nc]
            cur_len = recursion(matrix, visited, pos, 0)
            results.append(cur_len)
            print("append")
            j += 1
        i += 1

    return results

def recursion(matrix, visited, pos, cur_len):
    nr, nc = pos[2], pos[3]
    cr, cc = pos[0], pos[1]
    if visited[cr][cc] == True:
        return cur_len
    visited[cr][cc] = True
    if matrix[cr][cc]:
        cur_len += 1
        if cc + 1 < nc and not visited[cr][cc + 1]:
            new_pos = [cr, cc + 1, nr, nc]
            cur_len = recursion(matrix, visited, new_pos, cur_len)
        if cr + 1 < nr and not visited[cr + 1][cc]:
            new_pos = [cr + 1, cc, nr, nc]
            cur_len = recursion(matrix, visited, new_pos, cur_len)
        if cc - 1 > -1 and not visited[cr][cc - 1]:
            new_pos = [cr, cc - 1, nr, nc]
            cur_len = recursion(matrix, visited, new_pos, cur_len)
        if cr - 1 > -1 and not visited[cr - 1][cc]:
            new_pos = [cr - 1, cc, nr, nc]
            cur_len = recursion(matrix, visited, new_pos, cur_len)
    return cur_len
