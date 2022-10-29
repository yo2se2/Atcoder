from collections import deque

N, M = map(int, input().split())


v = [[False for _ in range(N)] for _ in range(N)]

# 進める移動先を列挙する。 O(N^2)
nxt = []
for k in range(N):
    for l in range(N):
        n = (k ** 2 + l ** 2)
        if n == M:
            if k != 0 and l != 0:
                nxt.append((k,l))
                nxt.append((k,-l))
                nxt.append((-k,-l))
                nxt.append((-k,l))
            elif k == 0:
                nxt.append((k,l))
                nxt.append((k,-l))
            else:
                nxt.append((k,l))
                nxt.append((-k,l))


def BFS(sx,sy,nxt):
    d = deque()
    d.append((sx,sy,0))
    v[sx][sy] = True
    m = [[-1 for _ in range(N)] for _ in range(N)]
    m[sx][sy] = 0
    while d:
        x, y , dis = d.popleft()
        for dx,dy in nxt:
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < N:
                if 0 <= ny and ny < N:
                    if not(v[nx][ny]):
                        d.append((nx,ny, dis+1))
                        v[nx][ny] = True
                        m[nx][ny] = dis + 1

    return m

ans = BFS(0,0,nxt)

for a in ans:
    print(' '.join(map(str,a)))