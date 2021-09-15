H, W = map(int, input().split())
M = []
a = ['.' for _ in range(W+2)]
score = [[0 for _ in range(W)] for _ in range(H)]
M.append(a)
for _ in range(H):
    s = list(input())
    M.append(['.']+s+['.'])
M.append(a)
n = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

#
for i in range(1,H+1):
    for j in range(1,W+1):
        if M[i][j] == '#':
            score[i-1][j-1] = '#'
        elif M[i][j] == '.':
            for dx,dy in n:
                if M[i+dy][j+dx] == '.':
                    continue
                elif M[i+dy][j+dx] == '#':
                    score[i-1][j-1] += 1
for i in score:
    print(''.join(map(str, i)))
