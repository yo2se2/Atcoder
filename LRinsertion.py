from collections import deque

N = int(input())
S = list(input())

d = deque([N])
p = 0

for i in range(N-1,-1,-1):
    if S[i] == 'L':
        d.append(i)
    elif S[i] == 'R':
        d.appendleft(i)
ans = list(d)
ans = list(map(str,ans))
print(' '.join(ans))