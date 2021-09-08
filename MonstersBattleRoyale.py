N = int(input())
A = list(map(int, input().split()))
f = [True for _ in range(N)]
div = min(A)
idx = A.index(div)
nd = div
L = len(A)
while L > 1:
    nA = []
    for i in range(L):
        if idx == i:
            nA.append(A[i])
        else:
            if A[i] % div != 0:
                nA.append(A[i] % div)
                if nd > A[i] % div:
                    nd = A[i] % div

    L = len(nA)
    A = nA
    div = nd
    idx = A.index(div)

print(A[0])


