import sys
sys.setrecursionlimit(10000)
R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
visited = [[False for _ in range(C)] for _ in range(R)]
dis = [[0 for _ in range(C)] for _ in range(R)]
map = []
for i in range(R):
    c = list(input())
    map.append(c)

def BFS(sy,sx,gy,gx,dis):
    #スタート地点をキューに代入,次点の定義(上下左右)
    queue = [(sy-1,sx-1)]
    next = [(0,1),(0,-1),(1,0),(-1,0)]


    while queue:
        #キューから取り出して，訪問済みもしくはゴールを判定
        y, x = queue.pop(0)
        if y == gy - 1 and x == gx -1:
            break
        if visited[y][x] == True:
            continue
        #訪問済みでなく，進行可能なら，次点をキューに追加し，距離を記録
        else:
            visited[y][x] = True
            for dy,dx in next:
                if map[y+dy][x+dx] == '.' and visited[y+dy][x+dx] == False:
                    queue.append((y+dy,x+dx))
                    dis[y+dy][x+dx] = dis[y][x] + 1
    return dis



answer = BFS(sy,sx,gy,gx,dis)

print(answer[gy-1][gx-1])
