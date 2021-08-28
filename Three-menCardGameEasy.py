from collections import deque

Sa = deque(list(input()))
Sb = deque(list(input()))
Sc = deque(list(input()))

T = {}

T['a'], T['b'], T['c'] = Sa, Sb, Sc

n = T['a'].popleft()

while T[n]:
    n = T[n].popleft()

print(n.upper())



