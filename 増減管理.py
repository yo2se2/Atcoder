N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

for i in range(1,N):
    if A[i] > A[i-1]:
        print('up {}'.format(A[i]-A[i-1]))
    elif A[i] < A[i-1]:
        print('down {}'.format(A[i-1] - A[i]))
    else:
        print('stay')