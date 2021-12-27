from collections import deque

N, X = map(int, input().split())
v = []
L  = []
f = []
A = []
for _ in range(N):
    s = deque(list(map(int, input().split())))
    l = s.popleft()
    L.append(l)
    v.append([False for _ in range(l)])
    A.append(list(s))
ans = 0

def DFS(x,p):
    global ans
    stack = []
    if x == N:
        if p == X:
            ans += 1
        return
    for a in A[x]:
        if p * a > X:
            continue
        DFS(x+1,p*a)


DFS(0,1)
print(ans)

