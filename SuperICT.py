S = input()

s = list(S)
l1 = ['I','C','T']
l2 = ['i','c','t']
i = 0
f = False

for c in s:
    if c == l1[i] or c == l2[i]:
        if i == 2:
            f = True
        else:
            i += 1

if f:
    print('YES')
else:
    print('NO')