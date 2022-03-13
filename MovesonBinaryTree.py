N, X = map(int, input().split())
S = input()
f = [True for _ in range(N)]


x = list(format(X,'b'))

for s in S:
    if s == 'U':
        if x:
            x.pop()
    elif s == 'L':
        x.append('0')
    elif s == 'R':
        x.append('1')
x = ''.join(x)
print(int(x,2))