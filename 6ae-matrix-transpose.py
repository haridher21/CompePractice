def transposeMatrix(matrix):
    n, m = len(matrix), len(matrix[0])
    matrix2 = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            matrix2[j][i] = matrix[i][j]
    return matrix2
