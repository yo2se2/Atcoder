N, T = map(int,input().split())

open = T
A = []
for _ in range(N):
    a = int(input())
    A.append(a)
diff = []
for i in range(1,N):
    if A[i-1] + T < A[i]:
        open += T
    else:
        open += A[i]-A[i-1]

print(open)
