from collections import Counter

X, N = map(int, input().split())
p = list(map(int, input().split()))

c = Counter(p)

i = 0
f = True
l = 1000
r = 1000

while f:
    if i + X < 101:
        if c[i+X] == 0:
            l = i + X
            f = False
    else:
        l = 101
        f = False

    if X - i > 0:
        if c[X-i] == 0:
            r = X - i
            f = False
    else:
        r = 0
        f = False
    i += 1

ans = min(l,r)
print(ans)