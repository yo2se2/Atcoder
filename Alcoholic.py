N, X = map(int, input().split())
V = []
P = []
a = 0

for _ in range(N):
    v, p = map(int, input().split())
    V.append(v)
    P.append(p)

up = X * 100
for i in range(N):
    a += V[i]*P[i]
    if a <= up:
        continue
    else:
        print(i+1)
        exit()
print(-1)