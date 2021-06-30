N, M, T = map(int, input().split())
n = N
s = 0
A = []
B = []
answer = 'Yes'
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(M):
    n = n  - (A[i] - s)
    if n > 0:
        n +=  (B[i] - A[i])
        n = min(N,n)
        s = B[i]
    else:
        print('No')
        exit()
n = n - (T - s)
if n > 0:
    print(answer)
else:
    print('No')


