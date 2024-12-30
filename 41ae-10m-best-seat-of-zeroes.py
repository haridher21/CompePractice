def bestSeat(seats): # O(N) T O(1) S
    if sum(seats) == len(seats):
        return -1
    last_zero, true_last_zero, max_zeroes, zero_count = None, None, 0, 0
    for i in range(1, len(seats)):
        if not seats[i]:
            zero_count += 1
            last_zero = i
        else:
            if not last_zero:
                continue
            if max_zeroes < zero_count:
                max_zeroes = zero_count
                true_last_zero = last_zero
            zero_count = 0
    return true_last_zero - (max_zeroes // 2)
