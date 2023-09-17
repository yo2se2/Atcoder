N = int(input())
S = list(input())

Q = int(input())
f = 0
d = {}

for _ in range(Q):
    t, x, c = map(str,input().split())

    if int(t) == 1:
        S[int(x)-1] = c
        d[int(x)-1] = c
    elif int(t) == 2:
        f = 2
        d = {}
    elif int(t) == 3:
        f = 3
        d = {}

if f == 0:
    print(''.join(S))
elif f == 2:
    ans = list(''.join(S).lower())
    for key in d:
        ans[key] = d[key]
    print(''.join(ans))
elif f == 3:
    ans = list(''.join(S).upper())
    for key in d:
        ans[key] = d[key]
    print(''.join(ans))
