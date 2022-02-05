from math import gcd

N, X = map(int, input().split())
x = list(map(int, input().split()))
d = []
for i in range(N):
    d.append(abs(x[i]-X))

g = d[0]

for i in range(1,N):
    g = gcd(g, d[i])

print(g)