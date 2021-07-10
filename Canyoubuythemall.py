N, X = map(int, input().split())
A = list(map(int, input().split()))

t = sum(A)
d = N // 2

if t-d <= X:
    print('Yes')
else:
    print('No')