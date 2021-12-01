N = int(input())
A = list(map(int, input().split()))

l = 0
ans = 0
while l < N:
    L = 0
    d = {}
    r = l

    while r < N:
        if A[r] in d.keys():
            l = d[A[r]] + 1
            break
        else:
            L += 1
            d[A[r]] = r
            r += 1
    ans = max(ans,L)
    if r > N-1:
        break

print(ans)