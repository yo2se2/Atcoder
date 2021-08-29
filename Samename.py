from collections import Counter

N = int(input())
S = []
T = []
f = False

name = []
for i in range(N):
    s, t = input().split()
    name.append("{} {}".format(s,t))

c = Counter(name)

for C in c:
    if c[C] >= 2:
        f = True
        break

if f:
    print('Yes')
else:
    print('No')