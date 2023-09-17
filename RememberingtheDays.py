N, M = map(int, input().split())
L = [[0 for _ in range(N+1)] for _ in range(N+1)]
n = [[] for _ in range(N+1)]
f = [False for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    L[a][b] = c
    L[b][a] = c
    n[a].append(b)
    n[b].append(a)
ans = 0

def DFS(x,s):
    global ans
    f[x] = True #再帰でおとずれた町を処理
    if s > ans:
        ans = s
    for nx in n[x]:
        if not f[nx] and L[x][nx]:
            DFS(nx,s+L[x][nx])
    f[x] = False #戻りの際,訪れた町をリセット

for i in range(1,N+1):
    DFS(i,0)

print(ans)

