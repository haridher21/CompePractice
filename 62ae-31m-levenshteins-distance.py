def levenshteinDistance(str1, str2): # O(NM) TS but Space still suboptimal
    # Also my logic is sorta not the right intuitive one
    l1, l2 = len(str1), len(str2)
    dp = [[max(i, j) for j in range(l2 + 1)] for i in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            diagonal = dp[i-1][j-1] if str1[i-1] == str2[j-1] else dp[i-1][j-1] + 1
            down = dp[i-1][j] if j > 1 and str1[i-1] == str2[j-2] else dp[i-1][j] + 1
            right = dp[i][j-1] if i > 1 and str1[i-2] == str2[j-1] else dp[i][j-1] + 1
            dp[i][j] = max(min(diagonal, down, right), dp[i-1][j-1])
    return dp[l1][l2]
