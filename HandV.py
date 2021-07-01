import copy
H, W, K = map(int,input().split())
init_c = []
for _ in range(H):
    c = list(input())
    init_c.append(c)

answer = 0
for i in range(2**(H+W)):
    bit = []
    for j in range(H+W):
        if (i>>j) & 1 == 1:
            bit.append(1)
        else:
            bit.append(0)
    colum = bit[:H]
    row = bit[H:]
    C = copy.deepcopy(init_c)
    for a in range(H):
        if colum[a] == 1:
            C[a] = ['x'] * W
    for b in range(W):
        if row[b] == 1:
            for c in range(H):
                C[c][b] ='x'
    cnt = 0
    for d in range(H):
        for e in range(W):
            if C[d][e] == '#':
                cnt += 1
                # print(cnt)

    if cnt == K:

        answer += 1
print(answer)

