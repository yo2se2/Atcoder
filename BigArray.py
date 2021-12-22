N, K = map(int, input().split())
d = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a in d:
        d[a] += b
    else:
        d[a] = b

sd = sorted(d)

i = 0
for k in sd:
    i += d[k]
    if i < K:
        continue
    else:
        ans = k
        break
print(ans)