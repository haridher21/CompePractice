def numberOfWaysToMakeChange(n, denoms): # O(ND) T O(N) S if N > logD else O(DlogD) TS
    # But can be done without n == 0 and j == denom condition, but yeah its optimal
    d = len(denoms)
    if n == 0 and d > 0:
        return 1
    denoms.sort()
    dp = [0 for _ in range(n + 1)]
    for denom in denoms:
        for j in range(1, n + 1):
            if j == denom:
                dp[j] = dp[j] + 1
            elif j > denom:
                dp[j] += dp[j - denom]
    return dp[n]

"""
def numberOfWaysToMakeChange(n, denoms): # O(N * D) if N > logD else O(DlogD) T S
    d = len(denoms)
    if n == 0 and d > 0:
        return 1
    denoms.sort()
    dp = [[0 for _ in range(n + 1)] for _ in range(d + 1)]
    for i in range(1, d + 1):
        denom = denoms[i - 1]
        for j in range(1, n + 1):
            if j == denom:
                dp[i][j] = dp[i-1][j] + 1
            elif j < denom:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - denom]
    return dp[d][n]
"""
