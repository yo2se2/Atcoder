N, K = map(int, input().split())

n = list(str(N))

def func(n: list):
    big = []
    small = []
    while n:
        max_value = max(n)
        max_idx = n.index(max_value)
        a = n.pop(max_idx)
        big.append(a)
    small =big[::-1]
    return int(''.join(big)), int(''.join(small))

for i in range(K):
    b, s = func(n)
    n = list(str((b - s)))

print(''.join(n))
