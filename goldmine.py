def rec(mine, i, j):
    n, m = len(mine), len(mine[0])
    if i == n or j < 0 or j == m:
        return 0
    else:
        return mine[i][j] + max(rec(mine, i+1, j-1), rec(mine, i+1, j), rec(mine, i+1, j+1))
 
 
def gold(mine):
    max_gold = 0
    for i in range(len(mine[0])):
        max_gold = max(max_gold, rec(mine, 0, i))
    return max_gold
 
 
def rec(mine, i, j, lookup):
    n, m = len(mine), len(mine[0])
    if (i, j) in lookup:
        return lookup[(i, j)]
    if i == n or j < 0 or j == m:
        return 0
    else:
        lookup[(i, j)] = mine[i][j] + max(rec(mine, i+1, j-1, lookup), rec(mine, i+1, j, lookup), rec(mine, i+1, j+1, lookup))
        return lookup[(i, j)]
 
 
def gold(mine):
    max_gold = 0
    lookup = {}
    for i in range(len(mine[0])):
        max_gold = max(max_gold, rec(mine, 0, i, lookup))
        return max_gold
 
 
def gold(mine):
    n, m = len(mine), len(mine[0])
    dp = [[0]*m for i in range(n)]
    for j in range(m):
        dp[0][j] = mine[0][j]
    for i in range(1, n):
        for j in range(m):
            top_left = dp[i-1][j-1] if (j-1) >= 0 else 0
            top = dp[i-1][j]
            top_right = dp[i-1][j+1] if (j+1) < m else 0
            dp[i][j] = mine[i][j] + max(top_left, top, top_right)
    return max(dp[n-1])
 
 
def gold(mine):
    n, m = len(mine), len(mine[0])
    prev_dp = [0]*m
    dp = [0]*m
    for j in range(m):
        prev_dp[j] = mine[0][j]
    for i in range(1, n):
        for j in range(m):
            top_left = prev_dp[j-1] if (j-1) >= 0 else 0
            top = prev_dp[j]
            top_right = prev_dp[j+1] if (j+1) < m else 0
            dp[j] = mine[i][j] + max(top_left, top, top_right)
        prev_dp = dp
        dp = [0]*m
    return max(prev_dp)