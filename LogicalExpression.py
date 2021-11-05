N = int(input())
S = []

for _ in range(N):
    s = input()
    S.append(s)

dp = [[0, 0] for _ in range(N+1)]
dp[0] = [1, 1]

for i in range(N):
    f = S[i]
    if f == 'AND':
        for j in [0, 1]:
            for k in [0, 1]:
                dp[i+1][j and k] += dp[i][k]
    else:
        for j in [0, 1]:
            for k in [0, 1]:
                dp[i+1][j or k] += dp[i][k]

print(dp[-1][1])

