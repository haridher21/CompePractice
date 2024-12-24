def tournamentWinner(competitions, results):
    d, n = {}, len(results)
    for i in range(n):
        if competitions[i][0] not in d:
            d[competitions[i][0]] = 0
        if competitions[i][1] not in d:
            d[competitions[i][1]] = 0
        if results[i] == 1:
            d[competitions[i][0]] += 3
        else:
            d[competitions[i][1]] += 3
    maxval = -1
    for k in d:
        if d[k] > maxval:
            maxval = d[k]
            winner = k
    return winner
            
