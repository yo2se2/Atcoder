n, X = map(int, input().split())
a = list(map(int, input().split()))

s = []
ans = 0
for i in range(n):
    if (X >> i) & 1 == 1:
        s.append(1)
        ans += a[i]
    else:
        s.append(0)
print(ans)
