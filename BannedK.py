from collections import Counter
from math import factorial


def comb(n, r):
    return factorial(n) // factorial(n - r) // factorial(r)


N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

d = {}
d2 = {}
sum = 0
for i in c:
    if c[i] > 1:
        d[i] = comb(c[i], 2)
        sum += d[i]
    if c[i] - 1 > 1:
        d2[i] = comb(c[i] - 1, 2)

for a in A:
    if a in d:
        if a in d2:
            diff = d[a] - d2[a]
        else:
            diff = d[a]
    else:
        diff = 0
    ans = sum - diff
    print(ans)
