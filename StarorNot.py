N = int(input())
n = [[] for _ in range(N+1)]
v = [False for _ in range(N+1)]

v[0] = True
ans = 'No'
for i in range(N-1):
    a, b = map(int,input().split())
    n[a].append(b)
    n[b].append(a)

for nl in n:
    if len(nl) == N-1:
        ans = 'Yes'

print(ans)