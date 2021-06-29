N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
v = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def BFS(s,g):
    cnt = 1
    q = []
    dis = [0] * (N + 1)
    root = [[] for _ in range(N+1)]

    if not v[s]:
        q.append(s)
        v[s] = True

    while q:
        n = q.pop(0)
        if n == g:
            break
        for i in node[n]:
            if not v[i]:
                v[i] = True
                root[i].append(n)
                dis[i] = dis[n] + 1
                q.append(i)
            else:
                continue

    return root

a = BFS(1,0)
if sum(v) == N:
    print('Yes')
    for i in range(2,N+1):
        print(a[i][0])
else:
    print('No')
