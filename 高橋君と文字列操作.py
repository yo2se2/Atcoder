from collections import deque

s = list(input())
t = list(input())
s = deque(s)
t = deque(t)
i = 0
L = len(s)
ans = -1

while i < L:
    if s == t:
        ans = i
        break
    elif s != t:
        temp = s.pop()
        s.appendleft(temp)

    i += 1
print(ans)