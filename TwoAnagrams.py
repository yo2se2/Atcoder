s = input()
t = input()
S = list(s)
T = list(t)

S.sort()
T.sort(reverse=True)

sd = ''.join(S)
td = ''.join(T)

if sd < td:
    print('Yes')
else:
    print('No')
