from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

C = Counter(A)

ans = '?'
h = N/2
for c in C:
    if C[c] > h:
        ans = c

print(ans)
