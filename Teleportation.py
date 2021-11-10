from math import gcd

N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

S = set()
for i in range(N):
    xi = X[i]
    yi = Y[i]
    for j in range(i+1,N):
        xj = X[j]
        yj = Y[j]
        dx = xi-xj
        dy = yi-yj
        g = gcd(dx,dy)
        S.add((dx/g,dy/g))
        S.add((dx/g*-1,dy/g*-1))
print(len(S))
