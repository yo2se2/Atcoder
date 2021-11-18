from collections import Counter
from  math import ceil
N, M = map(int, input().split())
name = input()
kit = input()

name_c = Counter(name)
kit_c = Counter(kit)

ans = 0
for c in name:
    if kit_c[c] == 0:
        ans = -1
        break
    else:
        cnt = ceil(name_c[c] / kit_c[c])
        if ans < cnt:
            ans = cnt
print(ans)