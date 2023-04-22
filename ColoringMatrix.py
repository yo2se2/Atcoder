from collections import deque
N = int(input())
A = []
B = []
m = []

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] == 1:
            m.append([i,j])
    A.append(a)
for _ in range(N):
    b = list(map(int, input().split()))
    B.append(b)

ans = 'No'
next = m
for k in range(4):
    f = True
    # print("{}回目".format(k))
    # print(next)
    stack = deque(next)
    next = []
    while stack:
        ci, cj = stack.popleft()
        ni, nj = cj, N-1-ci
        next.append([ni,nj])
        if f:
            if B[ci][cj] == 1:
                continue
            else:
                f = False
    if f:
        print('Yes')
        exit()
print('No')