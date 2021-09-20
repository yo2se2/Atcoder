N, W = map(int, input().split())

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(N):
    for j in range(W+1):
        if j >= weight[i]:
            dp[i+1][j] = max(dp[i][j],dp[i][j-weight[i]]+value[i])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[N][W])