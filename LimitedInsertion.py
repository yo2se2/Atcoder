from collections import deque

N = int(input())
b = list(map(int, input().split()))
ans = []
last = -1
cnt = N
Q = deque()
for _ in range(N):
    for i in range(cnt):
        if b[i] == i+1:
            last = i
    if last == -1:
        print(-1)
        exit()
    else:
        cnt -= 1
        Q.appendleft(b.pop(last))
        last = -1


for i in Q:
    print(i)

