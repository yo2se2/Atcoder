N, M = map(int, input().split())
n = [[] for _ in range(N+1)]
v = [False for _ in range(N+1)]
v[0] = True
ans = 0
for i in range(M):
    A, B = map(int,input().split())
    n[A].append(B)
    n[B].append(A)

def DFS(s,vis):
    stack = [s]
    while stack:
        x = stack.pop()
        vis[x] = True
        for dx in n[x]:
            if not(vis[dx]):
                stack.append(dx)
    return vis

for i in range(1,N+1):
    if not(v[i]):
        ans += 1
        DFS(i,v)

print(ans-1)