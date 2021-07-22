from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

ans = 'YES'

for i in c:
    if c[i] == 1:
        continue
    else:
        ans = 'NO'
        break
print(ans)