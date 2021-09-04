from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
cnt = 0
l = []
for i in c:
    if c[i] > 1:
        l.append(i)

l.sort(reverse=True)

if len(l) != 0:
    if c[l[0]] >= 4:
        ans = l[0]*l[0]
    elif len(l) >=2:
        ans = l[0] * l[1]
    else:
        ans = 0
else:
    ans = 0
print(ans)



