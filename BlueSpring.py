N, D, P = map(int, input().split())
F = list(map(int,input().split()))
F.sort()
c = 0
ns = [0]


for f in F:
    c += f
    ns.append(c)

n = N//D + 1
ans = n*P

for i in range(n):
    cost = i*P + ns[N-i*D]
    ans = min(ans, cost)

print(ans)