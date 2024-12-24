def nonConstructibleChange(coins):
    coins.sort()
    sum = 0
    for coin in coins:
        if coin - sum > 1:
            break
        sum += coin
    return sum + 1
