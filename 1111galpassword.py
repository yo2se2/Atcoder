#平坦数

N = int(input())

mod = 998244353
dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(1,10):
        if j == 1:
            dp[i][j] = (dp[i-1][2] + dp[i-1][1])%mod
        elif j == 9:
            dp[i][j] = (dp[i-1][8] + dp[i-1][9])%mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%mod
print(sum(dp[N])%mod)