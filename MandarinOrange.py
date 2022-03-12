N = int(input())
A = list(map(int, input().split()))

l = 0
r = 0
m = A[0]
ans = 0

for l in range(N):
    x = A[l]
    for r in range(l,N):
        x = min(x,A[r])
        s = x*(r-l+1)
        ans = max(ans, x*(r-l+1))

print(ans)