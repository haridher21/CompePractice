def sweetAndSavory(dishes, target):
    # O(NLOGN) T O(N) S cause of dishes
    # Split and sort for slightly more optimal solution
    n = len(dishes)
    if n < 2:
        return [0, 0]
    dishes.sort()
    i, j, cur_i, cur_j, best_sum = 0, n - 1, 0, 0, None
    while i < j and dishes[i] < 0 and dishes[j] > 0:
        sum = dishes[i] + dishes[j]
        if sum == target:
            cur_i, cur_j = i, j
            break
        elif sum < target:
            if best_sum == None:
                best_sum = sum
                cur_i, cur_j = i, j
            elif sum > best_sum:
                best_sum = sum
                cur_i, cur_j = i, j
            i += 1
        elif sum > target:
            j -= 1
    if cur_i == cur_j:
        return [0, 0]
    return [dishes[cur_i], dishes[cur_j]]
