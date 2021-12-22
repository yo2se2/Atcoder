from collections import Counter

S = list(input())
T = int(input())

c = Counter(S)

x = c['R']-c['L']
y = c['U']-c['D']
L = abs(x)+abs(y)

if T == 1:
    ans = L + c['?']
elif T == 2:
    if L <= c['?']:
        ans = (c['?']-L)%2
    else:
        ans = L - c['?']
print(ans)