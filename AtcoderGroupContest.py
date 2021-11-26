N = int(input())
a = list(map(int, input().split()))

A = sorted(a)

ans = 0
for i in range(1,N+1):
    ans += A[-2*i]

print(ans)