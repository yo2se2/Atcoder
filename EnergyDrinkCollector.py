N, M = map(int, input().split())
p = 0
L = []

for i in range(N):
    a, b = map(int, input().split())
    L.append((a,b))

L.sort(key=lambda x: x[0])

for i in range(N):
    if L[i][1] < M:
        p += L[i][0] * L[i][1]
        M -= L[i][1]

    else:
        p += L[i][0] * M
        M -= L[i][1]
        break

print(p)

