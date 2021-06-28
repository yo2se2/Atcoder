N = int(input())
A = list(map(int, input().split()))
L = len(A)


a = A.index(max(A[:L//2]))
b = A.index(max(A[L//2:]))

if A[a] > A[b]:
    print(b+1)
else:
    print(a+1)




