N, S = map(int, input().split())

dp = [[False for _ in range(N+1)] for _ in range(10010)]
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[j][i]:
            dp[j+A[i]][i+1] = (j,'H')
            dp[j+B[i]][i+1] = (j,'T')

if dp[S][N]:
    print('Yes')
    n = N
    s = S
    ans = ''
    while s != 0:
        d = dp[s][n][0]
        t = dp[s][n][1]
        ans += t
        s = d
        n -= 1
    print(ans[::-1])
else:
    print('No')
