from itertools import permutations

N, M = map(int, input().split())
T = [[False for _ in range(N)] for _ in range(N)]
A = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    T[a-1][b-1] = True
    T[b-1][a-1] = True

for _ in range(M):
    c, d = map(int, input().split())
    A[c-1][d-1] = True
    A[d-1][c-1] = True

ans = False
for p in permutations(range(N)):
    ok = True
    for i in range(N):
        for j in range(N):
            if T[i][j] != A[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print("Yes" if ans else "No")