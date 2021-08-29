from collections import deque

N, M = map(int, input().split())
n = [[] for _ in range(N+1)]
v = [False for _ in range(N+1)]
dis = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    n[a].append(b)
    n[b].append(a)

q = deque([1])

while q:
    x = q.popleft()
    v[x] = True
    if dis[x] == 2:
        break
    else:
        for nx in n[x]:
            if not(v[nx]):
                q.append(nx)
                dis[nx] = dis[x] + 1

if dis[N] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')