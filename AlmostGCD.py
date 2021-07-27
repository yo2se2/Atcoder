# 全探索

N = int(input())
A = list(map(int, input().split()))
L = len(A)
M = max(A)
ans = 0
div = -1

for i in range(2, M+1):
    gcd = 0
    for j in range(L):
        if A[j] % i == 0:
            gcd += 1

    if ans < gcd:
        ans = gcd
        div = i

print(div)
