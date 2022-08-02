import numpy as np

INF = 10**9

N, M = map(int, input().split())
X = list(map(int, input().split()))
b = np.zeros(N+1, np.int64)

for _ in range(M):
    c, y = map(int, input().split())
    b[c] = y


dp = np.zeros(N+1, np.int64)

for i in range(1,N+1):
    d0 = dp.max()
    # print(dp[:i],b[1:i+1],X[i-1])
    dp[1:i+1] = dp[:i] + X[i-1] + b[1:i+1]
    dp[0] = d0
print(dp.max())