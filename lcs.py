def lcs(s1, s2, i=0, j=0):
    if i == len(s1) or j == len(s2):
        return 0
    elif s1[i] == s2[j]:
        return 1 + lcs(s1, s2, i+1, j+1)
    else:
        return max(lcs(s1, s2, i+1, j), lcs(s1, s2, i, j+1))
 
 
def lcs(s1, s2, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i, j) in lookup:
        return lookup[(i, j)]
    if i == len(s1) or j == len(s2):
        return 0
    elif s1[i] == s2[j]:
        lookup[(i, j)] = 1 + lcs(s1, s2, i+1, j+1, lookup)
        return lookup[(i, j)]
    else:
        lookup[(i, j)] = max(lcs(s1, s2, i+1, j, lookup), lcs(s1, s2, i, j+1, lookup))
        return lookup[(i, j)]
 
 
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
 
 
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    prev_dp = [0]*(m+1)
    dp = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[j] = 1 + prev_dp[j-1]
            else:
                dp[j] = max(prev_dp[j], dp[j-1])
        prev_dp = dp
        dp = [0]*(m+1)
    return prev_dp[m]

