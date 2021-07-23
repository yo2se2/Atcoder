N, K = map(int, input().split())
S = []
for i in range(N):
    s = int(input())
    if s == 0:
        Max = N
    S.append(s)

if Max == N:
    print(N)
    exit()

for l in range(N-1):
    cnt = 0
    mul = S[l]
    if mul <= K:
        cnt += 1
        r = l + 1
        while mul*S[r] <= K:
            mul *= S[r]
            r += 1
            cnt += 1
    if Max < cnt:
        Max = cnt
print(Max)
