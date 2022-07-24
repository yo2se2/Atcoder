N, X, Y = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(2)]

dp[0][N] = 1

for i in range(N,1,-1):
    dp[1][i] += dp[0][i]*X
    dp[0][i-1] += dp[0][i]
    dp[0][i] = 0
    for j in range(i,1,-1):
        dp[0][j-1] += dp[1][j]
        dp[1][j-1] += dp[1][j] * Y
        dp[1][j] = 0

print(dp[1][1])