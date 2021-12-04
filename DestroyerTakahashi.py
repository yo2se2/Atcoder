N, D = map(int, input().split())
wall = [0 for _ in range(11)]
M = []
x = -10**10
for _ in range(N):
    L, R = map(int, input().split())
    M.append((L,R))

M.sort(key= lambda x: x[1])
cnt = 0

for m in M:
    l = m[0]
    r = m[1]

    if l > x + D - 1:
        cnt += 1
        x = r
print(cnt)

