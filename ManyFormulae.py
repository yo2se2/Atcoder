N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1

ans = [[0, 0] for _ in range(N)]
ans[0][0] = A[0]

for i, a in enumerate(A[1:]):
    dp[i+1][0] = (dp[i][0] + dp[i][1]) % MOD
    dp[i+1][1] = dp[i][0] % MOD

    ans[i+1][0] = (ans[i][0] + ans[i][1] + a * sum(dp[i])) % MOD
    ans[i+1][1] =  (ans[i][0] - a * dp[i][0]) % MOD

print((ans[N-1][0] + ans[N-1][1]) % MOD )