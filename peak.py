N, M = map(int, input().split())
H = list(map(int, input().split()))

f = [True for _ in range(N)]
node = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)
    if H[a-1] > H[b-1]:
        f[b-1] = False
    elif H[a-1] < H[b-1]:
        f[a-1] = False
    else:
        f[a - 1] = False
        f[b - 1] = False

print(sum(f))