N, M = map(int, input().split())
F = True
f = [False for _ in range(N)]
a = [0 for _ in range(N)]

if N != 1:
    a[0] = 1
for i in range(M):
    s, c = map(int, input().split())
    if not(f[s-1]):
        f[s-1] = True
        a[s-1] = c
    else:
        if a[s-1] == c:
            continue
        else:
            F = False

if N != 1 and a[0] == 0:
    F = False

if F:
    print(int(''.join(map(str,a))))
else:
    print(-1)

