N = int(input())
h = list(map(int, input().split()))

#足場i に行くまでの最小コストを収めるリスト
dp = [0 for _ in range(N)]

dp[0] = 0
for i in range(1,N):
    if i == 1:
        dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]),dp[i-2] + abs(h[i]-h[i-2]))

print(dp[N-1])