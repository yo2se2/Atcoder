H, W, C, Q = map(int, input().split())
query = []

Color = [0 for _ in range(C)]
for _ in range(Q):
    t, n, c = map(int, input().split())
    query.append((t,n,c))

r = 0
l = 0
row = {}
line = {}

for i in range(Q-1,-1,-1):

    t, n, c = query[i]
    # print(t,n,c)
    if t == 1:
        if n in row:
            continue
        else:
            Color[c-1] += W - r
            row[n] = 1
            l += 1
    elif t == 2:
        if n in line:
            continue
        else:
            Color[c-1] +=  H - l
            line[n] = 1
            r += 1

print(' '.join(list(map(str, Color))))