N = int(input())
f = [False for _ in range(10**5+10)]
ans = 0
for _ in range(N):
    a = int(input())
    if f[a]:
        ans += 1
    else:
        f[a] = True

print(ans)