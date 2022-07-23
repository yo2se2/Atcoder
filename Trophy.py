N, X = map(int, input().split())

A = []
B = []
C = []

c = 0

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    c += (a+b)
    C.append(c)

ans = float('inf')
for i in range(N):
    t = 0
    if i <= X:
        t = C[i] + B[i]*(X-(i+1))
        ans = min(ans,t)

    else:
        break
print(ans)





