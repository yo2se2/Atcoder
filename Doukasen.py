N = int(input())
A = []
B = []
t = [0]
x = [0]
csum = 0
for _ in range(N):
    a, b = map(int, input().split())
    csum += a
    x.append(csum)
    t.append(a/b)
    A.append(a)
    B.append(b)

lt = [0]
rt = [0]

for i in range(1,N+1):
    lt.append(t[i] + lt[i-1])
    rt.append(t[N+1-i] + rt[i-1])

lx = 1
rx = N

while lx < rx:
   if lt[lx] < rt[N+1-rx]:
       lx = lx + 1
   else:
       rx = rx - 1


v = B[lx-1]

T = (A[lx-1] + v*(lt[lx-1]+rt[N-rx])) / (2 * v)
ans = v*(T-lt[lx-1]) + x[lx-1]

print(ans)