def minWaitingTime(queries):
    queries.sort()
    n, sum = len(queries), 0
    for i in range(n-1):
        sum += queries[i] * (n - i - 1)
    return sum
