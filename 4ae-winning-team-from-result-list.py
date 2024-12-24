def tournamentWinner(competitions, results):
    d, n, maxval, winner = {}, len(results), -1, ""
    for i in range(n):
        if competitions[i][0] not in d:
            d[competitions[i][0]] = 0
        if competitions[i][1] not in d:
            d[competitions[i][1]] = 0
        if results[i] == 1:
            d[competitions[i][0]] += 3
            if d[competitions[i][0]] > maxval:
                maxval = d[competitions[i][0]]
                winner = competitions[i][0]
        else:
            d[competitions[i][1]] += 3
            if d[competitions[i][1]] > maxval:
                maxval = d[competitions[i][1]]
                winner = competitions[i][1]
    return winner
            
