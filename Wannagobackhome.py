S = list(input())

s = set(S)
l = len(s)

f = True

for c in s:
    if c == 'N':
        if not('S' in s):
            f = False
    if c == 'S':
        if not('N' in s):
            f = False
    if c == 'E':
        if not('W' in s):
            f = False
    if c == 'W':
        if not('E' in s):
            f = False
if f:
    print('Yes')
else:
    print('No')