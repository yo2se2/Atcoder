N, K = map(int, input().split())
S = []

for i in range(N):
    s = int(input())
    S.append(s)
r,  ans = 0, 0
mul = 1
cnt = 0
if 0 in S:
    print(N)
else:
    for l in range(N):
        while r < N and mul*S[r] <= K:
            mul *= S[r]
            r += 1

        ans = max(ans,r-l)
        if l == r:
            r += 1
        else:
            mul //= S[l]
    print(ans)


