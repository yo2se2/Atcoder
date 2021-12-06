S = list(input())
L = len(S)
a = [0 for _ in range(L)]
#ダブリンぐで10**5回後の位置を考える
dp = [[0 for _ in range(L)] for _ in range(33)]

for i in range(L):
    if S[i] == 'R':
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for i in range(32):
    for j in range(L):
        dp[i+1][j] = dp[i][dp[i][j]]

ans = [0 for _ in range(L)]
for i in range(L):
    ans[dp[32][i]] += 1
ans = map(str,ans)
print(' '.join(ans))