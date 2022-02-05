S = list(input())
t = []

for s in S:
    if s == '1':
        t.append('1')
    elif s == '0':
        t.append('0')
    elif s == 'B':
        if t:
            t.pop()
print(''.join(t))