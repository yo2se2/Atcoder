from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d = Counter(D)
f = True

for t in T:
    if t in d:
        d[t] -= 1
        if d[t] < 0:
            f = False
            break
    else:
        f = False
        break
if f:
    print('YES')
else:
    print('NO')
