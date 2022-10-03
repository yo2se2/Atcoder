from collections import deque

N, X, Y = map(int, input().split())
n = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int,input().split())
    n[u].append(v)
    n[v].append(u)

def DFS(s,e):
    stack = [s]
    vis = [False for _ in range(N + 1)]
    vis[s] = -1
    ans = deque()
    while stack:
        x = stack.pop()

        if x == e:
            ans.appendleft(x)
            nx = vis[x]
            while nx != -1:
                ans.appendleft(nx)
                nx = vis[nx]
            return list(ans)

        for dx in n[x]:
            if not(vis[dx]):
                stack.append(dx)
                vis[dx] = x

Ans = DFS(X,Y)
print(' '.join(list(map(str,Ans))))


