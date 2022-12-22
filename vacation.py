N = int(input())
h = []
for _ in range(N):
    a, b, c = map(int, input().split())
    h.append([a,b,c])

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0],dp[0][1],dp[0][2] = h[0][0],h[0][1],h[0][2]

for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][k] = max(dp[i][k],dp[i-1][j]+h[i][k])
print(max(dp[N-1]))

