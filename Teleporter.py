N, K =map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(61)]

# ダブリンぐ
for i in range(N):
    dp[0][i] = A[i]-1

for i in range(60):
    for j in range(N):
        dp[i+1][j] = dp[i][dp[i][j]]

a = []
for i in range(61):
    if K >> i & 1 == 1:
        a.append(i)
x = 0

for A in a:
    x = dp[A][x]

print(x+1)



