N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = {}
for i, a in enumerate(A):
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]

ans = []
for i in range(Q):
    x, k = map(int, input().split())
    if x in d:
        if len(d[x]) >= k:
            ans.append(d[x][k-1]+1)
        else:
            ans.append(-1)
    else:
        ans.append(-1)
for a in ans:
    print(a)


