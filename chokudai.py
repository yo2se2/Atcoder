S = list(input())
T = list('chokudai')
# 「Sのi文字目までを使って,chokudaiのj文字目まで選択する方法」
dp = [[0 for _ in range(9)] for _ in range(len(S)+1)]
for i in range(len(S)+1):
    dp[i][0] = 1

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] != T[j]:
            dp[i+1][j+1] = dp[i][j+1]
        elif S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
print(dp[-1][-1]%(10**9+7))
