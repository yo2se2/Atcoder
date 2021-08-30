from collections import deque
N = int(input())
cnt = 0
X = 0
Y = N
ans = []

def magic(X):
    q = deque([])
    if X % 2 != 0:
        X -= 1
        q.extendleft('A')

    while X % 2 == 0 and X > 0:
        X = X // 2
        q.extendleft('B')

    return X, q

X, Q = magic(N)

ans = []
while N > 0:
    N, Q = magic(N)
    ans = list(Q) + ans
    # print(N,Q)
print(''.join(ans))


