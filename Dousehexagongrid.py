N = int(input())

m = [[False for _ in range(2010)] for _ in range(2010)]
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x,y))
    m[x+1000][y+1000] = True

def DFS(sx,sy):
    if m[sx+1000][sy+1000]:
        stack = [(sx,sy)]
        m[sx+1000][sy+1000] = False
        cnt = 1

        d = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]
        while stack:
            x, y = stack.pop()
            for dx, dy in d:
                if m[x+1000+dx][y+1000+dy]:
                    stack.append((x+dx,y+dy))
                    m[x + 1000 + dx][y + 1000 + dy] = False
                    cnt += 1

        return 1
    else:
        return 0
ans = 0
for x,y in XY:
    c = DFS(x,y)
    ans += c
print(ans)


