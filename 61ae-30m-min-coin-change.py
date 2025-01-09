def minNumberOfCoinsForChange(n, denoms): # O(ND) T O(N) S Optimal
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0
    for denom in denoms:
        for change in range(n + 1):
            if denom <= change:
                dp[change] = min(dp[change], dp[change - denom] + 1)
    return dp[n] if dp[n] != float("inf") else -1
