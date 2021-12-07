N, M = map(int, input().split())
f = [True for _ in range(101010)]
dp = [0 for _ in range(101010)]
dp[0] = 1
mod = 10**9 + 7

for _ in range(M):
    a = int(input())
    f[a] = False

for i in range(N):
    if f[i+1]:
        dp[i+1] += dp[i]
    if f[i+2]:
        dp[i+2] += dp[i]

print(dp[N]%mod)

