N = int(input())
A = []
B = []
P = []
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a % b == 0:
        p = 0
    else:
        p = b-(a%b)
    B.append(b)
    P.append(p)

ans = 0
for i in range(N-1,-1,-1):
    temp = P[i]-ans
    if temp >= 0:
        ans += temp
    else:
        ans += temp % B[i]

print(ans)

