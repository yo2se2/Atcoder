H, W, N = map(int, input().split())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 座標圧縮　

cA = {x:i+1 for i,x in enumerate(sorted(set(A)))}
cB = {x:i+1 for i,x in enumerate(sorted(set(B)))}
for i in range(N):
    print(cA[A[i]],cB[B[i]])