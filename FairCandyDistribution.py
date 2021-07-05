N, K = map(int, input().split())
A = list(map(int, input().split()))
sA = sorted(A)
a = K // N
b = K % N
c = sA[b]

for i in range(N):
    if A[i] < c:
        print(a+1)
    else:
        print(a)
