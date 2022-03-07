H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

c = [[0 for _ in range(W)] for _ in range(H)]

a = 0

for i in range(H):
    if i % 2 == 0:
        for j in range(W):

            if A[a] == 0:
                a += 1

            c[i][j] = str(a+1)
            A[a] -= 1
    else:
        for j in range(W-1,-1,-1):

            if A[a] == 0:
                a += 1

            c[i][j] = str(a+1)
            A[a] -= 1

for i in range(H):
    s = ' '.join(c[i])
    print(s)



