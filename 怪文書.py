from collections import Counter
n = int(input())
S = []

per=''
for i in range(n):
    s = list(input())
    c = Counter(s)
    if i == 0:
        bc = c
    else:
        for str in bc:
            if c[str] > bc[str]:
                continue
            elif c[str] < bc[str]:
                bc[str] = c[str]

for c in bc:
    per += c*(bc[c])

ans = sorted(per)
print(''.join(ans))
