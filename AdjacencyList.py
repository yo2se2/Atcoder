N, M = map(int, input().split())
n = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    n[a].append(b)
    n[b].append(a)
for i in range(1,N+1):
    L = [len(n[i])]
    n[i].sort()

    print(' '.join(map(str, L+n[i])))

