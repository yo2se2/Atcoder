from collections import Counter

N, K = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)
score = 0
i = 0

while K > 0:
    if c[i] > 0:
        c[i] -= 1
        i += 1
    else:
        score += i
        i = 0
        K -= 1
        continue
print(score)
