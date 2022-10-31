from collections import defaultdict

N = int(input())
A = []
d = defaultdict(list)
s = set()
for _ in range(N):
    a = int(input())
    A.append(a)
    s.add(a)
L = list(s)
L.sort()
i = 0
for l in L:
    d[l] = i
    i += 1

for  a in A:
    print(d[a])

yo2