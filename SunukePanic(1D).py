N = int(input())
d = {}

for _ in range(N):
    t, x, a = map(int, input().split())
    T = t
    if x > t:
        continue
    else:
        d[t] = (x,a)

dp = [[0 for _ in range(5)] for _ in range(T+1)]

for i in d:
    dp[i][d[i][0]] = d[i][1]

for t in range(1,T+1):
    for j in range(5):
        if j == 0:
            dp[t][j] += max(dp[t - 1][j], dp[t - 1][j + 1])
        elif j == 4:
            dp[t][j] += max(dp[t - 1][j], dp[t - 1][j - 1])
        else:
            dp[t][j] += max(dp[t-1][j], dp[t-1][j-1], dp[t-1][j+1])
print(max(dp[-1]))

