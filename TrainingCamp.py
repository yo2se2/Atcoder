N = int(input())
mod = (10**9) + 7
ans = 1

for i in range(1,N+1):
    ans = (ans * i) % mod

print(ans)
