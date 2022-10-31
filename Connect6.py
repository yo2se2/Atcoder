N = int(input())
S = [input() for _ in range(N)]


def cal(x, y, dx, dy):
    cnt = 0
    for _ in range(6):
        if not(0 <= min(x,y) and max(x,y) < N):
            return False
        if S[x][y] == '#':
            cnt += 1
        x += dx
        y += dy
    return cnt >= 4
d = [(1,0),(0,1),(1,1),(-1,1)]

for i in range(N):
    for j in range(N):
        for dx, dy in d:
            if cal(i,j,dx,dy):
                print('Yes')
                exit()

print('No')