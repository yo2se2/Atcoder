N, M, X = map(int,input().split())
C = []
A = []
min = 10** 10
flag = True
for _ in range(N):
    ca = list(map(int,input().split()))
    C.append(ca[0])
    A.append(ca[1:])

for i in range(2**N):
    understand = [0 for _ in range(M)]
    cost = 0
    bit = []
    for j in range(N):
        if((i >> j) & 1) == 1:
            bit.append(1)
        else:
            bit.append(0)

    for idx,v in enumerate(bit):
        if v == 1:
            cost += C[idx]
            for m in range(M):
                understand[m] += A[idx][m]

    cnt = [True for judge in understand if judge >= X ].count(True)
    if i == (2**N-1) and cnt != M:
        min = -1
    if cnt == M and cost < min:
        min = cost

print(min)