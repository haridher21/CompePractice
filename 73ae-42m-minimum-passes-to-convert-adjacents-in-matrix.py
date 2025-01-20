def minimumPassesOfMatrix(matrix):
    # Optimal # O(RC) TS, but theirs is still better, but I had the right idea
    if not (len(matrix) and len(matrix[0])):
        return 0
    r, c, count, temp_negs = len(matrix), len(matrix[0]), 0, {}
    directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
    for i in range(r): # O(RC)
        for j in range(c):
            if matrix[i][j] < 0:
                adjacent_pos = False
                for dr, dc in directions:
                    tr, tc = i + dr, j + dc
                    if tr > -1 and tr < r and tc > -1 and tc < c:
                        if matrix[tr][tc] > 0:
                            adjacent_pos = True
                            break
                if adjacent_pos:
                    temp_negs[(i, j)] = matrix[i][j]
            else:
                count += 1
    if count == 0:
        return -1
    total, iterations = r * c, 0
    prev_temp_negs = temp_negs
    while count < total and prev_temp_negs: 
    # Until all -ve nums who are adjacent to a +ve num are converted, or can't convert anymore
        temp_negs = {}
        adjacent_neg = len(prev_temp_negs)
        iterations += 1
        count += adjacent_neg
        for i, j in prev_temp_negs: # Converting the current iteration of adjacent -ve nums
            matrix[i][j] *= -1
            for dr, dc in directions:
                tr, tc = i + dr, j + dc
                if tr > -1 and tr < r and tc > -1 and tc < c:
                    # The below dictionary checks happen in O(1), but yeah how dictionaries do it, idk
                    if matrix[tr][tc] < 0 and (tr, tc) not in temp_negs and (tr, tc) not in prev_temp_negs:
                        temp_negs[(tr, tc)] = matrix[tr][tc]
        prev_temp_negs = temp_negs
    return -1 if count < total else iterations
