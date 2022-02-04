N = int(input())

s = list(input())
t = list(input())
L = 2*N
ans = L
for i in range(N):
    if t[:i+1] == s[-(i + 1):]:
        ans = L - (i+1)

print(ans)

