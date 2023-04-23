N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
ans = 0

if T in C:
    M = 0
    for i in range(N):
        if C[i] == T:
            if R[i] > M:
                M = R[i]
                ans = i
else:
    M = R[0]
    for i in range(N):
        if C[0] == C[i]:
            if R[i] > M:
                M = R[i]
                ans = i
print(ans + 1)

