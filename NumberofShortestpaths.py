from collections import deque

N, M = map(int, input().split())
n = [[] for _ in range(N+1)]



for _ in range(M):
    a, b = map(int, input().split())
    n[a].append(b)
    n[b].append(a)


def BFS(s,g):
    q = deque([])
    v = [False for _ in range(N + 1)]
    t = [0 for _ in range(N + 1)]
    cnt = [0 for _ in range(N + 1)]
    cnt[s] = 1
    if not v[s]:
        q.append(s)
        v[s] = True

    while q:
        x = q.popleft()


        for dx in n[x]:
            if not v[dx]:
                q.append(dx)
                v[dx] = True
                t[dx] = t[x] + 1
                cnt[dx] = cnt[x]
            elif t[dx] == t[x] + 1:
                cnt[dx] += cnt[x]
                cnt[dx] %= 10**9+7

    return cnt[g]

print(BFS(1,N))


