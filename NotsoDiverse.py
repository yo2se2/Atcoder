from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
l = len(c)
C  = c.most_common()
ans = 0

while l > K:
    ans += C.pop()[1]
    l -= 1

print(ans)