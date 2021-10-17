from collections import deque

S = list(input())
d = deque(S)
LisS = [''.join(S)]
for i in range(len(S)):
    s = d.pop()
    d.appendleft(s)
    LisS.append(''.join(d))

LisS.sort()

print(LisS[0])
print(LisS[-1])